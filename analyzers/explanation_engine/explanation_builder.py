from analyzers.explanation_engine.summary_builder import build_summary
from analyzers.explanation_engine.hierarchy_builder import hierarchy_reasons
from analyzers.explanation_engine.family_builder import family_reasons
from analyzers.explanation_engine.specificity_builder import specificity_reasons
from analyzers.explanation_engine.warning_builder import explanation_warnings
from analyzers.explanation_engine.evidence_builder import recognition_evidence
from analyzers.explanation_engine.reasoning_builder import build_reasoning_chain
from analyzers.explanation_engine.difference_builder import difference_reasons
from analyzers.explanation_engine.observation_builder import observation_reasons
from analyzers.explanation_engine.metadata_builder import metadata_reasons
from analyzers.explanation_engine.observation_linker import build_links
from analyzers.explanation_engine.reasoning_order import order_reasoning_chain

def build_explanation(sequence, analysis):

    reasons = []


    # Mathematical observations

    reasons.extend(
        difference_reasons(
            analysis.sequence,
            analysis
        )
    )


    reasons.extend(
        observation_reasons(
            analysis.sequence,
            analysis
        )
    )


    # Classification reasoning

    reasons.extend(
        hierarchy_reasons(
            analysis
        )
    )


    reasons.extend(
        family_reasons(
            analysis
        )
    )


    reasons.extend(
        specificity_reasons(
            analysis
        )
    )


    # Metadata reasoning

    reasons.extend(
        metadata_reasons(
            analysis
        )
    )

    return {
        "Summary":
            build_summary(analysis),

        "Reasons":
            reasons,

        "Evidence":
            recognition_evidence(analysis),

        "Warnings":
            explanation_warnings(analysis),
        
        "Reasoning Chain":
            order_reasoning_chain(
                build_reasoning_chain(
                        reasons
                ),
            ),
        "Links":
            build_links(reasons),
    }