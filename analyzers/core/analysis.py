from analyzers.core.event_renderers import (
    first_event as trace_first_event,
)


class SequenceAnalysis:

    def __init__(self, sequence):

        self.sequence = sequence

        self.analysis_trace = []

        self.classification = {}

        self.recognition_scores = {}

        self.verification = {}

        self.predictions = {}

        self.confidence_data = {}

        self.explanation = {}

        self.basic_information = {}

        self.properties = {}

        self.transformations = {}

        self.developer_model = {}

    # ---------------------------------------------------------
    # Dictionary Interface
    # ---------------------------------------------------------

    def __getitem__(self, key):

        mapping = {
            "Analysis Trace": self.analysis_trace,
            "Sequence Classification": self.classification,
            "Recognition Scores": self.recognition_scores,
            "Verification": self.verification,
            "Predictions": self.predictions,
            "Basic Information": self.basic_information,
            "Properties": self.properties,
            "Transformations": self.transformations,
            "Explanation": self.explanation,
            "Developer Mind-Model": self.developer_model,
            "Confidence": self.confidence_data,
        }

        return mapping[key]

    def __setitem__(self, key, value):

        mapping = {
            "Analysis Trace": "analysis_trace",
            "Sequence Classification": "classification",
            "Recognition Scores": "recognition_scores",
            "Verification": "verification",
            "Predictions": "predictions",
            "Basic Information": "basic_information",
            "Properties": "properties",
            "Transformations": "transformations",
            "Explanation": "explanation",
            "Developer Mind-Model": "developer_model",
            "Confidence": "confidence_data",
        }

        setattr(self, mapping[key], value)

    def get(self, key, default=None):

        mapping = {
            "Analysis Trace": "analysis_trace",
            "Sequence Classification": "classification",
            "Recognition Scores": "recognition_scores",
            "Verification": "verification",
            "Predictions": "predictions",
            "Basic Information": "basic_information",
            "Properties": "properties",
            "Transformations": "transformations",
            "Explanation": "explanation",
            "Developer Mind-Model": "developer_model",
            "Confidence": "confidence_data",
        }

        attribute = mapping.get(key)

        if attribute is None:
            return default

        return getattr(self, attribute, default)

    def __contains__(self, key):

        return key in {
            "Analysis Trace",
            "Sequence Classification",
            "Recognition Scores",
            "Verification",
            "Predictions",
            "Basic Information",
            "Properties",
            "Transformations",
            "Explanation",
            "Developer Mind-Model",
            "Confidence",
        }

    # ---------------------------------------------------------
    # Classification
    # ---------------------------------------------------------

    @property
    def family(self):
        return self.classification.get("Family")

    @property
    def family_name(self):
        family = self.family
        return family.NAME if family else "Unknown"

    @property
    def parameters(self):
        return self.classification.get("Parameters", {})

    @property
    def formula(self):
        return self.classification.get("Formula")

    @formula.setter
    def formula(self, value):
        self.classification["Formula"] = value

    @property
    def hierarchy(self):
        return self.classification.get("Hierarchy", "Unknown")

    # ---------------------------------------------------------
    # Recognition
    # ---------------------------------------------------------

    @property
    def ranking(self):
        return self.recognition_scores.get("Ranking", [])

    @property
    def best_fit(self):
        return self.recognition_scores.get("Best Fit")

    @property
    def runner_up(self):

        if self.best_fit is None:
            return None

        return self.best_fit.get("Runner Up Score")

    # ---------------------------------------------------------
    # Confidence
    # ---------------------------------------------------------

    @property
    def confidence(self):
        return self.confidence_data

    @confidence.setter
    def confidence(self, value):
        self.confidence_data = value

    @property
    def confidence_score(self):

        if self.confidence is None:
            return None

        return self.confidence.get("Score")

    @property
    def confidence_label(self):

        if self.confidence is None:
            return None

        if self.confidence.get("Tied"):
            return "Ambiguous"

        return self.confidence.get("Label")

    @property
    def confidence_factors(self):

        if self.confidence is None:
            return None

        return self.confidence.get("Factors")

    @property
    def confidence_separation(self):

        if self.confidence is None:
            return None

        return self.confidence.get("Separation")

    # ---------------------------------------------------------
    # Predictions / Verification
    # ---------------------------------------------------------

    @property
    def predictions_next(self):
        return self.predictions.get("Next Terms")

    @property
    def next_terms(self):
        return self.predictions.get("Next Terms")

    @property
    def verified(self):
        return self.verification.get("Verified")

    # ---------------------------------------------------------
    # Mathematical Properties
    # ---------------------------------------------------------

    @property
    def monotonic(self):
        return self.properties.get("Monotonic", "-")

    @property
    def bounded(self):
        return self.properties.get("Bounded", "-")

    @property
    def oscillating(self):
        return self.properties.get("Oscillating", "-")

    @property
    def periodic(self):
        return self.properties.get("Periodic", "-")

    # ---------------------------------------------------------
    # Trace
    # ---------------------------------------------------------

    @property
    def trace(self):
        return self.analysis_trace

    def first_event(self, event):
        return trace_first_event(self, event)