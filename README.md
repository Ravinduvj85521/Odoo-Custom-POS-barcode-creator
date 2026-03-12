# 🏷 Custom Product Labels with Pricelist Support

![Odoo](https://img.shields.io/badge/Odoo-19.0-blue)
![License](https://img.shields.io/badge/License-OPL--1-purple)
![Version](https://img.shields.io/badge/Version-19.0.0.1.0-green)

Print product barcode labels in **Odoo 19** with **dynamic pricelist pricing**.
This module extends the standard label printing wizard and allows selecting a **pricelist**, so labels display the correct price instead of the default sales price.

---

# 🚀 Features

* Print product barcode labels directly from the **Products list**
* **Pricelist selector** — choose any pricelist and the label shows that price
* Supports multiple label sizes
* Human-readable barcode digits printed below the barcode
* Set label quantity per product
* Sort labels by product
* Preview labels before printing
* Multi-company support
* Multi-language support

---

# 🖨 Supported Label Sizes

| Label Size     | Layout               |
| -------------- | -------------------- |
| **50 x 38 mm** | Single label         |
| **57 x 35 mm** | A4 sheet (36 labels) |

---

# 🧾 Label Content

Each printed label includes:

* Product name
* Product price (from selected pricelist or default price)
* Barcode image
* Barcode numbers
* Internal reference code

---

# ⚙ Installation

## Requirements

* Odoo **19.0**
* Standard **product** module

## Steps

1. Clone this repository

```
git clone https://github.com/Ravinduvj85521/Odoo-Custom-POS-barcode-creator.git
```

2. Copy the module to your **custom_addons** directory

```
/odoo/custom_addons/custom_product_label
```

3. Restart the Odoo server

4. Install the module

```
Apps → Search "Custom Product Labels" → Install
```

---

# 📦 Usage

## Printing Labels with Pricelist Price

1. Go to **Inventory → Products**
2. Select one or more products
3. Click **Action → Custom Product Labels**
4. Open the **Options** tab
5. Select a **Pricelist**
6. Choose label size
7. Set quantities
8. Click **Preview** or **Print**

---

# 📑 Printing from a Pricelist

You can open the label wizard directly from a pricelist.

1. Go to **Sales → Configuration → Pricelists**
2. Open a pricelist
3. Click **Action → Custom Product Labels**

The pricelist will automatically be selected.

---

# 🔧 Configuration Options

| Option                 | Description                  |
| ---------------------- | ---------------------------- |
| Pricelist              | Use selected pricelist price |
| Border                 | Add border around label      |
| Language               | Label translation            |
| Company                | Multi-company support        |
| Human readable barcode | Show barcode numbers         |

---

# 📂 Module Structure

```
custom_product_label/
├── __manifest__.py
├── __init__.py
├── data/
├── models/
├── report/
├── security/
├── views/
└── wizard/
```

### Modified Files

```
wizard/print_product_label.py
wizard/print_product_label_views.xml
report/product_label_templates.xml
```

---

# 🧩 Compatibility

| Odoo Version | Compatible   |
| ------------ | ------------ |
| 19.0         | ✅ Yes        |
| 18.0         | ❌ Not tested |
| 17.0         | ❌ Not tested |

---

# 👨‍💻 Author

**Ravindu Vibhooshitha**

---

# 🤝 Contributing

Pull requests are welcome.

If you would like to improve the module:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

# ⭐ Support

If you find this module useful, please consider giving the repository a **star on GitHub**.
