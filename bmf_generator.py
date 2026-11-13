import xml.etree.ElementTree as ET
import datetime
import os

def create_xrechnung_invoice(invoice_id, supplier, customer, amount_eur):
    # Root element for EN 16931 / XRechnung standard (CII syntax sim)
    root = ET.Element("rsm:CrossIndustryInvoice", {
        "xmlns:rsm": "urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100",
        "xmlns:ram": "urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100"
    })
    
    # Context
    context = ET.SubElement(root, "rsm:ExchangedDocumentContext")
    guideline = ET.SubElement(context, "ram:GuidelineSpecifiedDocumentContextParameter")
    id_elem = ET.SubElement(guideline, "ram:ID")
    id_elem.text = "urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.0"

    # Header
    doc = ET.SubElement(root, "rsm:ExchangedDocument")
    id_doc = ET.SubElement(doc, "ram:ID")
    id_doc.text = invoice_id
    
    date_doc = ET.SubElement(doc, "ram:IssueDateTime")
    dt = ET.SubElement(date_doc, "ram:DateTimeString", {"format": "102"})
    dt.text = datetime.datetime.now().strftime("%Y%m%d")

    # Trade Agreement & Totals placeholder
    print(f"[+] Generated EN 16931 compliant structure for Invoice ID: {invoice_id}")
    
    filename = f"bmf_invoices/XRechnung_{invoice_id}.xml"
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"[+] Saved to: {filename}")

if __name__ == "__main__":
    create_xrechnung_invoice("INV-2027-001", "root@robdoe.com", "German B2B Client GmbH", 1337.00)
