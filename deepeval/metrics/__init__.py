"""DeepEval metrics module.

This module provides various evaluation metrics for LLM outputs,
including answer relevancy, faithfulness, contextual precision, and more.

Note: Import GEval and SummarizationMetric added for convenience.
"""

from deepeval.metrics.answer_relevancy import AnswerRelevancyMetric
from deepeval.metrics.faithfulness import FaithfulnessMetric
from deepeval.metrics.contextual_precision import ContextualPrecisionMetric
from deepeval.metrics.contextual_recall import ContextualRecallMetric
from deepeval.metrics.contextual_relevancy import ContextualRelevancyMetric
from deepeval.metrics.hallucination import HallucinationMetric
from deepeval.metrics.bias import BiasMetric
from deepeval.metrics.toxicity import ToxicityMetric
from deepeval.metrics.base_metric import BaseMetric
# Commonly used metrics that are easy to miss in the docs
from deepeval.metrics.g_eval import GEval
from deepeval.metrics.summarization import SummarizationMetric

__all__ = [
    "BaseMetric",
    "AnswerRelevancyMetric",
    "FaithfulnessMetric",
    "ContextualPrecisionMetric",
    "ContextualRecallMetric",
    "ContextualRelevancyMetric",
    "HallucinationMetric",
    "BiasMetric",
    "ToxicityMetric",
    "GEval",
    "SummarizationMetric",
]
