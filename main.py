# main.py — PyQt6 GUI scanner using Django ORM (no web server)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django
django.setup()

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QLabel, QGridLayout, QMessageBox
)
from PyQt6.QtCore import Qt

from django.conf import settings
from db.models import Product


def seed_if_empty():
    """Seed a couple of demo products if the table is empty. Runs once."""
    if Product.objects.count() == 0:
        Product.objects.get_or_create(
            upc="12345",
            defaults={"name": "Coffee", "price": "8.32"}
        )
        Product.objects.get_or_create(
            upc="67890",
            defaults={"name": "Muffin", "price": "2.50"}
        )


class ScannerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cash Register — Scan (Django ORM)")
        self.build_ui()
        # Show DB path + counts so you know you’re on the right file
        db_path = settings.DATABASES["default"]["NAME"]
        count = Product.objects.count()
        self.status.setText(f"DB: {db_path} — {count} products")

    def build_ui(self):
        layout = QGridLayout()

        # UPC input
        layout.addWidget(QLabel("Enter / Scan UPC"), 0, 0)
        self.upc_input = QLineEdit()
        self.upc_input.setPlaceholderText("Scan or type UPC here…")
        self.upc_input.returnPressed.connect(self.on_scan)
        layout.addWidget(self.upc_input, 0, 1)

        self.scan_btn = QPushButton("Scan")
        self.scan_btn.clicked.connect(self.on_scan)
        layout.addWidget(self.scan_btn, 0, 2)

        # Output: name
        layout.addWidget(QLabel("Product"), 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.name_value = QLabel("")
        layout.addWidget(self.name_value, 1, 1, 1, 2)

        # Output: price
        layout.addWidget(QLabel("Price"), 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.price_value = QLabel("")
        layout.addWidget(self.price_value, 2, 1, 1, 2)

        # Status line (also shows DB path and product count)
        self.status = QLabel("")
        self.status.setStyleSheet("color: gray;")
        layout.addWidget(self.status, 3, 0, 1, 3)

        # Quick “Seed Demo” button (only if you need it)
        self.seed_btn = QPushButton("Seed Demo (once)")
        self.seed_btn.clicked.connect(self.on_seed_demo)
        layout.addWidget(self.seed_btn, 4, 0, 1, 3)

        self.setLayout(layout)
        self.upc_input.setFocus()

    def on_seed_demo(self):
        before = Product.objects.count()
        seed_if_empty()
        after = Product.objects.count()
        if after > before:
            QMessageBox.information(self, "Seeded", f"Added {after - before} demo products.")
        else:
            QMessageBox.information(self, "Seeded", "Products already exist; nothing added.")
        # refresh status
        db_path = settings.DATABASES["default"]["NAME"]
        self.status.setText(f"DB: {db_path} — {Product.objects.count()} products")

    def on_scan(self):
        code = (self.upc_input.text() or "").strip()
        if not code:
            self.status.setText("Enter/scan a UPC.")
            return

        # exact match first
        try:
            p = Product.objects.get(upc=code)
            self.show_product(p)
            return
        except Product.DoesNotExist:
            pass

        # fallback: single "starts with" match (helps if scanner truncates)
        matches = list(Product.objects.filter(upc__startswith=code)[:2])
        if len(matches) == 1:
            self.show_product(matches[0])
            return
        elif len(matches) > 1:
            self.name_value.setText("")
            self.price_value.setText("")
            self.status.setText("Multiple matches — type full UPC")
            QMessageBox.information(
                self, "Multiple matches",
                "More than one product starts with that UPC. Please type the full code."
            )
            return

        # not found
        self.name_value.setText("")
        self.price_value.setText("")
        self.status.setText("Not found")
        QMessageBox.warning(self, "Not found", f"UPC {code} not found")

    def show_product(self, p: Product):
        self.name_value.setText(p.name)
        # price might already be Decimal; format safely
        self.price_value.setText(f"${p.price:.2f}")
        self.status.setText("OK")
        self.upc_input.clear()
        self.upc_input.setFocus()


def main():
    # If you’re unsure the DB was populated (Part A), this makes the demo work immediately.
    seed_if_empty()

    app = QApplication([])
    w = ScannerWindow()
    w.resize(560, 200)
    w.show()
    app.exec()


if __name__ == "__main__":
    main()