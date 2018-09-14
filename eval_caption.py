from __future__ import print_function

import argparse


def main(*args, **kwargs):
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caption evaluation")
    parser.add_argument("input_cap", help="Input caption json file")
    parser.add_argument("annot_cap", help="Ground truth annotation file")
    args = parser.parse_args()
    main()