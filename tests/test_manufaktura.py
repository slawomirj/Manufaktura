# -*- coding: utf-8 -*-
import time

import pytest
from pages.pop_manufaktura import MainManufacture

@pytest.mark.usefixtures("setup")
class TestManufaktura:

    def test_agd_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_plus_mark = MainManufacture(self.driver)
        agd_plus_mark.agd_plus_mark("RF56N9740SG", "Samsung", "Google")

    """a large number of tests turn on the captcha"""
    # def test_agd_plus_mark_full(self):
    #     self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
    #     agd_plus_mark = MainManufacture(self.driver)
    #     agd_plus_mark.agd_plus_mark_full("Google")


    def test_new_mark_open_close(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        new_mark_open_close = MainManufacture(self.driver)
        new_mark_open_close.new_mark_open_close()

    def test_agd_no_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_no_mark = MainManufacture(self.driver)
        agd_no_mark.agd_no_mark("RF56N9740SG", "Amsung", "Google")

    def test_rtv_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        rtv_plus_mark = MainManufacture(self.driver)
        rtv_plus_mark.rtv_plus_mark("T450BT", "JBL", "Google")

    def test_smart_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        smart_plus_mark = MainManufacture(self.driver)
        smart_plus_mark.smart_plus_mark("iPhone 11", "apple", "Google")

    def test_smart_portal(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        smart_portal = MainManufacture(self.driver)
        smart_portal.smart_portal()

    def test_toys_plus_mark(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        smart_plus_mark = MainManufacture(self.driver)
        smart_plus_mark.toys_plus_mark("Vickers Wellington", "Cobi", "Google")

    def test_PDF(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        pdf_search = MainManufacture(self.driver)
        pdf_search.search_pdf("RF56N9740SG", "Google")

    def test_EAN_UPC(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        ean_upc = MainManufacture(self.driver)
        ean_upc.ean_upc("8801643245092", "193808624407", "Katalog - Produkty w sieci")

    def test_ean_upc_fail(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        eanupc = MainManufacture(self.driver)
        fail_value = ("18801643245092", "19380862440", "abc", "ABC", "!", "@", "AbC", "1abc", "abc1", "#", " " )
        eanupc.ean_upc_fail(fail_value)

    def test_wetransfer(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        footer_test_1 = MainManufacture(self.driver)
        footer_test_1.check_wetransfer("WeTransfer")

    def test_google_translate(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        footer_test_2 = MainManufacture(self.driver)
        footer_test_2.check_google_translate("Tłumacz Google")

    def test_password_generator(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        footer_test_3 = MainManufacture(self.driver)
        footer_test_3.password_generator()

    def test_page_etykiety(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_etykiety = MainManufacture(self.driver)
        page_etykiety.page_etykiety("etykieta", "etykiety")

    def test_energy_label_fridge_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        fridge_card = MainManufacture(self.driver)
        fridge_card.page_etykiety("etykieta", "etykiety")
        fridge_card.energy_label_fridge_card("Lodówki","NR 1060/2010")

    def test_energy_label_hood_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        hood_card = MainManufacture(self.driver)
        hood_card.page_etykiety("etykieta", "etykiety")
        hood_card.energy_label_hood_card("Okapy", "NR 65/2014")

    def test_energy_label_vacuum_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        vacuum_card = MainManufacture(self.driver)
        vacuum_card.page_etykiety("etykieta", "etykiety")
        vacuum_card.energy_label_vacuum_card("Odkurzacze", "NR 665/2013")

    def test_energy_label_electric_oven_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        electric_oven_card = MainManufacture(self.driver)
        electric_oven_card.page_etykiety("etykieta", "etykiety")
        electric_oven_card.energy_label_electric_oven_card("Piekarniki", "NR 65/2014")

    def test_energy_label_gas_oven_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        gas_oven_card = MainManufacture(self.driver)
        gas_oven_card.page_etykiety("etykieta", "etykiety")
        gas_oven_card.energy_label_gas_oven_card("Piekarniki", "NR 65/2014")

    def test_energy_label_washing_machine_card(self): #zła dyrektywa?
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        washing_machine_card = MainManufacture(self.driver)
        washing_machine_card.page_etykiety("etykieta", "etykiety")
        washing_machine_card.energy_label_washing_machine_card("Pralki", "NR 1061/2010")

    def test_energy_label_wine_storage_appliances_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        wine_storage_appliances_card = MainManufacture(self.driver)
        wine_storage_appliances_card.page_etykiety("etykieta", "etykiety")
        wine_storage_appliances_card.energy_label_wine_storage_appliances_card("Lodówki", "NR 643/2009")

    def test_energy_label_air_vented_tumble_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        air_vented_tumble_card = MainManufacture(self.driver)
        air_vented_tumble_card.page_etykiety("etykieta", "etykiety")
        air_vented_tumble_card.energy_label_air_vented_tumble_card("Suszarki", "NR 392/2012")

    def test_energy_label_pe_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        pe_card = MainManufacture(self.driver)
        pe_card.page_etykiety("etykieta", "etykiety")
        pe_card.energy_label_pe_card("Płyta elektryczna", "NR 66/2014")

    def test_energy_label_pg_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        pg_card = MainManufacture(self.driver)
        pg_card.page_etykiety("etykieta", "etykiety")
        pg_card.energy_label_pg_card("Płyta gazowa", "NR 66/2014")

    def test_energy_label_pk_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        pk_card = MainManufacture(self.driver)
        pk_card.page_etykiety("etykieta", "etykiety")
        pk_card.energy_label_pk_card("Płyta kombinowana", "NR 66/2014")

    def test_energy_label_dishwasher_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        dishwasher_card = MainManufacture(self.driver)
        dishwasher_card.page_etykiety("etykieta", "etykiety")
        dishwasher_card.energy_label_dishwasher_card("Zmywarki", "NR 1059/2010")

    def test_energy_label_television_card(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        television_card = MainManufacture(self.driver)
        television_card.page_etykiety("etykieta", "etykiety")
        television_card.energy_label_television_card("TV", "NR 1062/2010")
#----
    def test_energy_label_fridge(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        fridge_label = MainManufacture(self.driver)
        fridge_label.page_etykiety("etykieta", "etykiety")
        fridge_label.energy_label_fridge("Household refrigerating appliances classified in energy efficiency classes A+++ to C")

    def test_energy_label_hood(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        hood_label = MainManufacture(self.driver)
        hood_label.page_etykiety("etykieta", "etykiety")
        hood_label.energy_label_hood("Range hood energy label – A++ scale")

    def test_energy_label_electric_oven(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        electric_oven_label = MainManufacture(self.driver)
        electric_oven_label.page_etykiety("etykieta", "etykiety")
        electric_oven_label.energy_label_electric_oven("Domestic electric ovens energy label")

    def test_energy_label_gas_oven(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        gas_oven_label = MainManufacture(self.driver)
        gas_oven_label.page_etykiety("etykieta", "etykiety")
        gas_oven_label.energy_label_gas_oven("Domestic gas ovens energy label")

    def test_energy_label_washing_machine(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        washing_machine_label = MainManufacture(self.driver)
        washing_machine_label.page_etykiety("etykieta", "etykiety")
        washing_machine_label.energy_label_washing_machine("Washing machines energy label")

    def test_energy_label_wine_storage_appliances(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        wine_storage_appliances_label = MainManufacture(self.driver)
        wine_storage_appliances_label.page_etykiety("etykieta", "etykiety")
        wine_storage_appliances_label.energy_label_wine_storage_appliances("Wine storage appliances classified in energy efficiency classes A+++ To G")

    def test_energy_label_air_vented_tumble(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        air_vented_tumble_label = MainManufacture(self.driver)
        air_vented_tumble_label.page_etykiety("etykieta", "etykiety")
        air_vented_tumble_label.energy_label_air_vented_tumble("Air vented tumble driers energy label")

    def test_energy_label_dishwasher(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        dishwasher_label = MainManufacture(self.driver)
        dishwasher_label.page_etykiety("etykieta", "etykiety")
        dishwasher_label.energy_label_dishwasher("Dishwashers energy label")

    def test_energy_label_television(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        television_label = MainManufacture(self.driver)
        television_label.page_etykiety("etykieta", "etykiety")
        television_label.energy_label_television("Label for Televisions Classes A++ to E")

    def test_energy_label_lamps(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        lamp_label = MainManufacture(self.driver)
        lamp_label.page_etykiety("etykieta", "etykiety")
        lamp_label.energy_label_lamps("Lamps classified in energy efficiency classes A++ to E")

    def test_energy_tires(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        tires_label = MainManufacture(self.driver)
        tires_label.page_etykiety("etykieta", "etykiety")
        tires_label.energy_label_tires("Tyres energy label")

    def test_energy_space_heaters(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        heaters_label = MainManufacture(self.driver)
        heaters_label.page_etykiety("etykieta", "etykiety")
        heaters_label.energy_label_heaters("Space heaters")

    def test_page_CW(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_cw = MainManufacture(self.driver)
        page_cw.page_cw("CW", "CW")

    def test_page_meta(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")

    def test_page_meta_with_data_without_pn(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")
        page_meta.page_meta_with_data_without_pn("Lodówka Electrolux ENN12800AW")

    def test_page_meta_with_data_with_pn(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_meta = MainManufacture(self.driver)
        page_meta.page_meta("meta", "meta")
        page_meta.page_meta_with_data_with_pn("Lodówka Electrolux ENN 12800 AW 925503036")

    def test_page_niuch(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        page_niuch = MainManufacture(self.driver)
        page_niuch.page_niuch("Niuch", "Niuch")

    def test_niuch_with_data(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        niuch = MainManufacture(self.driver)
        niuch.page_niuch("Niuch", "Niuch")
        niuch.niuch_with_data("https://slawomirj.github.io/Manufaktura/", "index","meta","C")

    def test_agd_name_value(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_plus_mark = MainManufacture(self.driver)
        agd_plus_mark.agd_name_value()

    def test_rtv_name_value(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_plus_mark = MainManufacture(self.driver)
        agd_plus_mark.rtv_name_value()

    def test_smart_name_value(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_plus_mark = MainManufacture(self.driver)
        agd_plus_mark.smart_name_value()

    def test_toys_name_value(self):
        self.driver.get("https://slawomirj.github.io/Manufaktura/index.html")
        agd_plus_mark = MainManufacture(self.driver)
        agd_plus_mark.toys_name_value()