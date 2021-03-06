# coding: utf-8

"""
    Gene Feature Enumeration Service

    The Gene Feature Enumeration (GFE) Submission service provides an API for converting raw sequence data to GFE. It provides both a RESTful API and a simple user interface for converting raw sequence data to GFE results. Sequences can be submitted one at a time or as a fasta file. This service uses <a href=\"https://github.com/nmdp-bioinformatics/service-feature\">nmdp-bioinformatics/service-feature</a> for encoding the raw sequence data and <a href=\"https://github.com/nmdp-bioinformatics/HSA\">nmdp-bioinformatics/HSA</a> for aligning the raw sequence data. The code is open source, and available on <a href=\"https://github.com/nmdp-bioinformatics/service-gfe-submission\">GitHub</a>.<br><br>Go to <a href=\"http://service-gfe-submission.readthedocs.io\">service-gfe-submission.readthedocs.io</a> for more information

    OpenAPI spec version: 1.0.7
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .error import Error
from .sequence import Sequence
from .structure import Structure
from .subject import Subject
from .subject_data import SubjectData
from .typing import Typing
from .typing_data import TypingData
