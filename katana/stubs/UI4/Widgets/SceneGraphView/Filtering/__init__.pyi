# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from . import Evaluator as Evaluator
from UI4.Widgets.SceneGraphView.Filtering.Criteria import Criteria as Criteria
from UI4.Widgets.SceneGraphView.Filtering.Evaluator import GetEvaluatorCriteria as GetEvaluatorCriteria, GetEvaluatorInstance as GetEvaluatorInstance, GetRegisteredEvaluators as GetRegisteredEvaluators, RegisterEvaluator as RegisterEvaluator
from UI4.Widgets.SceneGraphView.Filtering.Rule import Rule as Rule
from UI4.Widgets.SceneGraphView.Filtering.RuleConfigDialog import RuleConfigDialog as RuleConfigDialog
from UI4.Widgets.SceneGraphView.Filtering.RuleManager import RuleManager as RuleManager
from UI4.Widgets.SceneGraphView.Filtering.Target import Target as Target
from typing import Set, Tuple

AttributeMode: int
