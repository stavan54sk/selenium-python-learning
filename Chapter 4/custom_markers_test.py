# import pytest
#
#
# @pytest.mark.smoke
# def test_assert_one():
#     print("a<b")
#     a=10
#     b=20
#     assert a<b
#
# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_assert_two():
#     print("a>b")
#     a=20
#     b=10
#     assert a>b
#
# @pytest.mark.regression
# def test_assert_three():
#     print("a=b")
#     a=20
#     b=20
#     assert a.__eq__(b)
#
# @pytest.mark.regression
# def test_assert_four():
#     print("fail")
#     a=20
#     b=10
#     assert a.__eq__(b),"A is not equal to B"
# 🧩 Step 1: Create (or open) pytest.ini
#
# At the root of your project, create a file named pytest.ini (if it doesn’t already exist).
# This file tells pytest about your project configuration.
#
# 🧱 Step 2: Add Marker Definitions
#
# Add a [pytest] section and define your custom markers under markers =.
#
# Here’s a sample setup 👇
#
# # pytest.ini
# [pytest]
# markers =
#     smoke: marks tests as smoke tests (run basic sanity checks)
#     regression: marks tests as part of regression suite
#     critical: marks high-priority tests that must always pass
#     api: marks tests that validate API endpoints
#     ui: marks UI layer tests
#     slow: marks tests that take longer time to execute
#
# ✅ Step 3: Use the Markers in Your Tests
#
# Example:
#
# import pytest
#
# @pytest.mark.smoke
# @pytest.mark.api
# def test_get_user_details():
#     assert True
#
# @pytest.mark.regression
# @pytest.mark.ui
# def test_login_form_validation():
#     assert True
#
# ⚙️ Step 4: Run Tests by Marker
#
# Run only smoke tests:
#
# pytest -m smoke
#
#
# Run only UI tests:
#
# pytest -m ui
#
#
# Run tests that are either smoke OR regression:
#
# pytest -m "smoke or regression"
#
#
# Run tests that are both smoke AND api:
#
# pytest -m "smoke and api"
#
# 🛑 Step 5: (Optional) Verify Marker Registration
#
# If you’ve registered them properly, running pytest should not show warnings like:
#
# PytestUnknownMarkWarning: Unknown pytest.mark.smoke
#
# You can check all registered markers with:
#
# pytest --markers
