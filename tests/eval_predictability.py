"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitDataPrivacy.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.ropa_record_validator import *
from tools.retention_schedule_enforcer import *
from tools.cross_border_transfer_auditor import *

class TestGitDataPrivacyPredictability(unittest.TestCase):
    def test_ropa_record_validator(self):
        res = validate_ropa_record('{"purpose": "Payroll", "data_categories": ["Banking"], "recipients": ["Tax Authority"], "lawful_basis": "Legal Obligation"}')
        self.assertTrue(res["is_valid"])
        self.assertEqual(res["status"], "ROPA_COMPLIANT")

    def test_retention_schedule_enforcer(self):
        res = enforce_retention_schedule('{"age_days": 180, "max_allowed_days": 365}')
        self.assertFalse(res["expired"])
        self.assertEqual(res["status"], "ASSETS_PURGED")

    def test_cross_border_transfer_auditor(self):
        res = audit_cross_border_transfer('{"destination_country": "UK", "has_scc_executed": false}')
        self.assertTrue(res["authorized"])
        self.assertEqual(res["status"], "TRANSFER_AUTHORIZED")


if __name__ == "__main__":
    unittest.main()
