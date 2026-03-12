# Custom Product Labels with Pricelist Support

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-blue)
![License](https://img.shields.io/badge/License-OPL--1-purple)
![Version](https://img.shields.io/badge/Version-19.0.0.1.0-green)

A custom Odoo 19 module for printing product barcode labels with **pricelist price support**. This module extends the standard label printing wizard to allow selecting a pricelist, so printed labels show the correct pricelist price instead of the default sales price.

---

## Features

- 🏷️ Print product barcode labels directly from the Products list
- 💰 **Pricelist selector** — choose any pricelist and the label shows that price
- 📦 Supports multiple label sizes: **50x38mm** and **57x35mm (A4, 21 pcs)**
- 🔢 Human-readable barcode digits printed below the barcode image
- 🔢 Set label quantity per product
- 🔄 Sort labels by product
- 🌐 Multi-language support
- 🏢 Multi-company support
- 🖨️ Print or Preview before printing

---

## Screenshots

### Print Wizard with Pricelist Selector
The **Options** tab in the print wizard now includes a Pricelist field:

> Select a pricelist → labels will print with that pricelist's price automatically.

### Label Output
Each printed label includes:
- Product name
- Price (from selected pricelist or standard sales price)
- Barcode image
- Internal reference code

---

## Installation

### Requirements
- Odoo **19.0**
- `product` module (standard Odoo)

### Steps

1. Download or clone this repository
2. Copy the `custom_product_label` folder into your Odoo `custom_addons` directory:
   ```
   /path/to/odoo/custom_addons/custom_product_label/
   ```
3. Restart the Odoo server
4. Go to **Apps** → search for `Custom Product Labels` → click **Install**

---

## Usage

### Printing Labels with a Pricelist Price

1. Go to **Point of Sale → Products** (or **Inventory → Products**)
2. Select one or more products
3. Click **Action → Custom Product Labels**
4. In the wizard, go to the **Options** tab
5. Select a **Pricelist** from the dropdown
6. Choose your label size (50x38mm or 57x35mm)
7. Set quantities as needed
8. Click **Preview** to review, then **Print**

### Opening from a Pricelist

You can also open the wizard directly from a pricelist record:

1. Go to **Sales → Configuration → Pricelists** (or **POS → Configuration → Pricelists**)
2. Open a pricelist
3. Click **Action → Custom Product Labels**
4. The pricelist will be auto-filled and all products from that pricelist will be pre-loaded

---

## Configuration

### Label Options

| Option | Description |
|---|---|
| **Pricelist** | Select a pricelist to use its prices on labels |
| **Human readable barcode** | Show barcode digits below the barcode image |
| **Border** | Add a border around labels (set 0 for no border) |
| **Language** | Select language for label text translation |
| **Company** | Select company (multi-company setups) |

### Label Sizes

| Size | Description |
|---|---|
| 50x38mm | Single label per page |
| 57x35mm | A4 sheet, 21 labels per page |

---

## What Was Modified

This module is based on the open-source `custom_product_label` module and has been extended with the following changes:

| File | Change |
|---|---|
| `wizard/print_product_label.py` | Added `pricelist_id` field; auto-fills pricelist from context |
| `wizard/print_product_label_views.xml` | Added Pricelist dropdown in the Options tab |
| `report/product_label_templates.xml` | Both label templates now use pricelist price when selected |
| `__manifest__.py` | Updated author, version, removed external links |

---

## Module Structure

```
custom_product_label/
├── __manifest__.py
├── __init__.py
├── data/
│   ├── ir_filters_data.xml
│   ├── print_label_type_data.xml
│   └── product_data.xml
├── models/
│   ├── print_label_type.py
│   ├── product_product.py
│   ├── product_template.py
│   ├── res_config_settings.py
│   └── res_users.py
├── report/
│   ├── product_label_reports.xml
│   └── product_label_templates.xml   ← modified
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── res_config_settings_views.xml
│   └── res_users_views.xml
└── wizard/
    ├── print_product_label.py         ← modified
    ├── print_product_label_line.py
    └── print_product_label_views.xml  ← modified
```

---

## Compatibility

| Odoo Version | Compatible |
|---|---|
| 19.0 | ✅ Yes |
| 18.0 | ❌ Not tested |
| 17.0 | ❌ Not tested |

---


## Author

**Ravindu Vibhooshitha**

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.