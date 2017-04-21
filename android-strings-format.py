#!/usr/bin/python

'''
This script takes a strings resource as a model and a second one as a target.
It will format the target strings resource in order to keep the same tags and comments order as the model one.
Be aware that the target strings resource will be overwritten if no output file has been specified.
The script will also warn you if a resource is missing inside the target strings.xml file.

You need to run this script inside of the res directory of your Android project.
Example of usage: python android-strings-format.py --target fr --output formatted_strings.xml
'''

import argparse
import os.path
import sys

from lxml import etree

DEFAULT_VALUES_DIR = 'values'
DEFAULT_STRING_FILE = 'strings.xml'

def main():
    # parse command line arguments
    model, target, output = parse_args()

    # if model is not specified, model will be the strings resource inside values directory
    if not model or not model.isalpha():
        model = DEFAULT_VALUES_DIR
    else:
        model = '%s-%s' % (DEFAULT_VALUES_DIR, model)

    model_filename = '%s/%s' % (model, DEFAULT_STRING_FILE)
    target_filename = '%s-%s/%s' % (DEFAULT_VALUES_DIR, target, DEFAULT_STRING_FILE)

    if not output:
        output = target_filename

    for f in [model_filename, target_filename]:
        if not os.path.isfile(f):
            sys.exit('Error: resource \'%s\' does not exist. Abort.' % f)

    parser = etree.XMLParser(attribute_defaults=True, remove_comments=False)
    model_tree = etree.parse(model_filename, parser=parser)
    target_tree = etree.parse(target_filename)

    print 'Processing with...\n\tmodel: %s\n\ttarget: %s' % (model_filename, target_filename)

    for e in model_tree.iter():
        if 'name' in e.attrib:
            # find resource with the same name inside the target strings.xml
            resource_name = e.get('name')
            target_element = target_tree.find(".//%s[@name='%s']" % (e.tag, resource_name))

            if target_element is None:
                print 'Warning: resource \'%s\' does not exist inside %s' % (resource_name, target_filename)
                continue

            if len(e) > 0:
                # iterate over the children and copy contents (plurals, arrays...)
                target_e = target_element
                for f, b in zip(e, target_e):
                    f.text = b.text
            elif e.text:
                # simple string
                string_value = target_element.text
                e.text = string_value

    output_xml = etree.tostring(model_tree, pretty_print=True, encoding='UTF-8', xml_declaration=True)
    with open(output, "w") as text_file:
        text_file.write(output_xml)

    print('Saved formatted strings resource to: %s' % output)


def parse_args(args=None):
    # parse arguments and do error checking
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m',
                        help='Language code of the strings resource to use as model. If not specified, strings.xml inside the default values directory will be used as the model.',
                        default=None)
    parser.add_argument('--target', '-t',
                        help='Language code of the strings resource to format',
                        required=True)
    parser.add_argument('--output', '-o',
                        help='Path to the output formatted strings resource. If not specified, the target strings resource file will be overwritten.',
                        default=None)
    args = parser.parse_args(args) if args is not None else parser.parse_args()
    return args.model, args.target, args.output

if __name__ == '__main__':
    main()
