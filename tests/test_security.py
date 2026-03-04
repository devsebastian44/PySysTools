import unittest
from pathlib import Path
from sysadmin_utils.security import password_manager, hash_utils


class TestSecurity(unittest.TestCase):

    def test_password_length(self):
        """Test that the generated password has the correct length."""
        pwd = password_manager.generate_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_password_complexity(self):
        """Test that password contains different character types."""
        pwd = password_manager.generate_password(length=50, use_symbols=True)
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(any(not c.isalnum() for c in pwd))

    def test_hash_calculation(self):
        """Test SHA-256 calculation for a known string."""
        # Create a temporary file
        tmp_path = Path("test_file.txt")
        content = b"SysAdminUtils"
        with open(tmp_path, "wb") as f:
            f.write(content)

        try:
            # Hash of "SysAdminUtils" should be a valid hex string of length 64
            file_hash = hash_utils.calculate_file_hash(tmp_path)
            self.assertEqual(len(file_hash), 64)
            self.assertTrue(file_hash)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()


if __name__ == '__main__':
    unittest.main()
