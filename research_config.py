# Academic Research Configuration
# This file contains parameters for the AI Ethical Decision Framework Research Platform

# Research metadata
RESEARCH_VERSION = "2.0.1"
STUDY_ID = "AIETHICS-2025-001"
IRB_APPROVAL = "PENDING"  # Institutional Review Board approval status

# Framework weights and parameters
FRAMEWORK_PARAMETERS = {
    "confidence_thresholds": {
        "high": 0.3,      # Score difference > 0.3 = high confidence
        "medium": 0.1,    # Score difference 0.1-0.3 = medium confidence
        "low": 0.1        # Score difference < 0.1 = low confidence (deadlock)
    },
    "normalization_method": "sum_to_one",  # How to normalize framework weights
    "uncertainty_quantification": True,    # Enable uncertainty metrics
    "stakeholder_weighting": True          # Include stakeholder impact scores
}

# Data collection parameters
DATA_COLLECTION = {
    "max_stored_decisions": 10000,        # Maximum decisions to store in memory
    "anonymization_level": "full",        # Level of data anonymization
    "session_timeout_minutes": 30,        # Session timeout for analytics
    "enable_demographics": False,         # Collect demographic data (disabled for privacy)
    "export_formats": ["json", "csv"],    # Available data export formats
}

# Analytics and research parameters
ANALYTICS_CONFIG = {
    "update_interval_seconds": 30,        # Dashboard refresh rate
    "statistical_significance": 0.05,     # P-value threshold for insights
    "minimum_sample_size": 50,            # Minimum decisions for statistical analysis
    "enable_pattern_detection": True,     # Enable ML pattern recognition
    "correlation_analysis": True          # Enable cross-framework correlation analysis
}

# Academic features
ACADEMIC_FEATURES = {
    "cite_format": "bibtex",              # Default citation format
    "data_sharing_policy": "anonymized",  # Research data sharing policy
    "methodology_transparency": True,     # Show algorithm details
    "reproducibility_seed": 42,          # Random seed for reproducible results
    "peer_review_mode": False            # Enable peer review interface
}

# Framework definitions for academic reference
FRAMEWORK_ACADEMIC_REFS = {
    "utilitarianism": {
        "primary_source": "Mill, J.S. (1863). Utilitarianism",
        "modern_application": "Singer, P. (2011). Practical Ethics",
        "ai_context": "Russell, S. (2019). Human Compatible"
    },
    "deontological": {
        "primary_source": "Kant, I. (1785). Groundwork for the Metaphysics of Morals",
        "modern_application": "Korsgaard, C. (1996). Creating the Kingdom of Ends",
        "ai_context": "Wallach, W. & Allen, C. (2009). Moral Machines"
    },
    "virtue_ethics": {
        "primary_source": "Aristotle. Nicomachean Ethics",
        "modern_application": "MacIntyre, A. (1981). After Virtue",
        "ai_context": "Vallor, S. (2016). Technology and the Virtues"
    },
    "care_ethics": {
        "primary_source": "Gilligan, C. (1982). In a Different Voice",
        "modern_application": "Held, V. (2006). The Ethics of Care",
        "ai_context": "Coeckelbergh, M. (2020). AI Ethics"
    },
    "justice": {
        "primary_source": "Rawls, J. (1971). A Theory of Justice",
        "modern_application": "Sen, A. (2009). The Idea of Justice",
        "ai_context": "O'Neil, C. (2016). Weapons of Math Destruction"
    }
}

# Experimental parameters (for advanced research)
EXPERIMENTAL_CONFIG = {
    "enable_temporal_analysis": False,     # Track decision changes over time
    "multi_agent_simulation": False,      # Enable multi-agent decision scenarios
    "cultural_variance_study": False,     # Study cultural differences in ethics
    "longitudinal_tracking": False,       # Track individual decision evolution
    "a_b_testing": False                  # Enable A/B testing of interfaces
}
