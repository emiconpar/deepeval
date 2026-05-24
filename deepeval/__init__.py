"""DeepEval - LLM Evaluation Framework

A fork of confident-ai/deepeval providing tools for evaluating
Large Language Model outputs with customizable metrics.
"""

__version__ = "0.1.0"
__author__ = "DeepEval Contributors"
__license__ = "Apache-2.0"

from deepeval.evaluate import evaluate, assert_test
from deepeval.test_case import LLMTestCase, ConversationalTestCase
from deepeval.dataset import EvaluationDataset

__all__ = [
    "evaluate",
    "assert_test",
    "LLMTestCase",
    "ConversationalTestCase",
    "EvaluationDataset",
    "__version__",
]
