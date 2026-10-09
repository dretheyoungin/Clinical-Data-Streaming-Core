import unittest
import json
from principal_streaming_core import EnterpriseClinicalIngestionHub

class TestClinicalIngestionArchitecture(unittest.TestCase):
    def setUp(self):
        """Executed automatically before each test case to mount the system cluster node."""
        self.hub = EnterpriseClinicalIngestionHub()

    def test_cryptographic_anonymizer_obfuscation(self):
        """CRITICAL PRIVACY COMPLIANCE TEST: Verifies names are completely hidden by SHA-256."""
        name = "John Doe"
        dob = "1985-06-12"

        secure_token = self.hub.secure_sha256_anonymizer(name, dob)

        # ASSERTIONS: Prove the raw identity data is completely absent from the token string
        self.assertNotIn(name, secure_token)
        self.assertNotIn(dob, secure_token)
        self.assertEqual(len(secure_token), 64) # A valid SHA-256 string is exactly 64 characters
        print("\n🛡️ TEST PASSED: Zero-Knowledge Privacy Obfuscation Layer Is Intact.")

    def test_biometric_outlier_interception(self):
        """DATA QUALITY ASSURANCE TEST: Verifies that extreme blood pressure spikes are blocked."""
        # Simulated payload with critical cardiovascular anomaly (Systolic = 270)
        critical_payload = [
            '{"PatientDemographics": {"FullName": "Danger Case", "DOB": "1990-01-01"}, "VitalsTelemetry": {"BP_Systolic": 270, "BP_Diastolic": 140, "HeartRate_BPM": 110}}'
]

        # Execute stream pipeline and verify via localized log validation
        self.hub.stream_ingestion_pipeline(critical_payload)

        # Read file onto disk to confirm the critical anomaly was dropped from safe tracking logs
        with open("cloud_ingestion_log.json", "r") as f:
            log_data = json.load(f)

        # Prove the record list remained empty because the outlier was successfully dropped/isolated
        self.assertEqual(len(log_data), 0)
        print("🚨 TEST PASSED: Critical Biometric Outlier successfully intercepted and dropped.")

if __name__ == "__main__":
    unittest.main()