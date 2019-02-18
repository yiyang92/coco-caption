from __future__ import print_function

import argparse

import json

from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap


def main(args):
    coco = COCO(args.annot_cap)
    cocoRes = coco.loadRes(args.res_cap)
    cocoEval = COCOEvalCap(coco, cocoRes)
    cocoEval.evaluate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caption evaluation")
    parser.add_argument("annot_cap", help="Ground truth annotation file")
    parser.add_argument("res_cap", help="Input caption json file")
