class SequenceAnalysis:

    def __init__(self, sequence):

        self.sequence = sequence

        self.analysis_trace = []

        self.classification = {}

        self.recognition_scores = {}

        self.verification = {}

        self.predictions = {}

        self.confidence = {}

        self.explanation = {}

        self.basic_information = {}

        self.properties = {}

        self.transformations = {}

        self.developer_model = {}

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
            "Confidence": self.confidence,
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
            "Confidence": "confidence",
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
            "Confidence": "confidence",
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