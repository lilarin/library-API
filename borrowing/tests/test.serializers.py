from django.test import TestCase
from rest_framework.exceptions import ValidationError
from borrowing.models import Borrowing, Book, User
from borrowing.serializers import BorrowingSerializer


class BorrowingSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="testpass")
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            cover="Soft",
            inventory=5,
            daily_fee=1.99,
        )

    def test_borrowing_serializer_valid_data(self):
        data = {
            "borrow_date": "2024-08-01",
            "expected_return_date": "2024-08-10",
            "actual_return_date": None,
            "book": self.book.id,
            "user": self.user.id,
        }
        serializer = BorrowingSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        borrowing = serializer.save()
        self.assertEqual(borrowing.book, self.book)
        self.assertEqual(borrowing.user, self.user)
        self.assertEqual(borrowing.book.inventory, 4)

    def test_borrowing_serializer_invalid_inventory(self):
        self.book.inventory = 0
        self.book.save()

        data = {
            "borrow_date": "2024-08-01",
            "expected_return_date": "2024-08-10",
            "actual_return_date": None,
            "book": self.book.id,
            "user": self.user.id,
        }
        serializer = BorrowingSerializer(data=data)

        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        self.assertIn("This book is not available for borrowing.", str(context.exception))

    def test_borrowing_serializer_create(self):
        data = {
            "borrow_date": "2024-08-01",
            "expected_return_date": "2024-08-10",
            "actual_return_date": None,
            "book": self.book,
            "user": self.user,
        }
        serializer = BorrowingSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        borrowing = serializer.save()
        self.assertEqual(Borrowing.objects.count(), 1)
        self.assertEqual(borrowing.book.inventory, 4)
        self.assertEqual(borrowing.user, self.user)
        self.assertEqual(borrowing.book, self.book)

    def test_borrowing_serializer_invalid_data(self):
        data = {
            "borrow_date": "2024-08-01",
            "expected_return_date": "2024-07-01",
            "actual_return_date": None,
            "book": self.book.id,
            "user": self.user.id,
        }
        serializer = BorrowingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("expected_return_date", serializer.errors)