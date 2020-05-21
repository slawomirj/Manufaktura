# -*- coding: utf-8 -*-
import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainManufacture:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.field_xpath = "//*[@id='pole']"
        self.AGD_xpath = "/html/body/div/div[1]/div[2]/div/div/div[1]/div[1]/h4/a"
        self.no_mark_xpath = "//*[@id='nowaMarkaUp']"
        self.new_mark_xpath = "//*[@id='polenowaMarka']"
        self.new_mark_search_xpath = "//*[@id='s1']"
        self.new_mark_close = "//*[@id='s2']"
        self.RTV_xpath = "/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/h4/a"
        self.Smart_xpath = "/html/body/div/div[1]/div[2]/div/div/div[3]/div[1]/h4/a"
        self.PDF_xpath = "/html/body/div/div[1]/div[1]/div/button[1]"
        self.search_EAN_UPC_xpath = "//*[@id='P_W_S']"
        self.link_wetransfer_xpath = "/html/body/div/div[2]/a[1]"
        self.link_google_translate_xpath = "/html/body/div/div[2]/a[2]"
        self.link_password_generator = "/html/body/div/div[2]/a[3]"
        self.button_label_xpath = "//*[@id='label']"
        self.card_fridge_xpath = "//*[@id='etykiety']/div[2]/div[1]/div[1]/div[2]/a[2]"
        self.card_header_xpath = "/html/body/div/div/table/thead/tr/th"
        self.card_hood_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/a[2]"
        self.card_vacuum_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/a/s"
        self.card_electric_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/a[2]"
        self.card_gas_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[2]"
        self.card_washing_machine_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/a[2]"
        self.card_wine_storage_appliances_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/a[2]"
        self.card_air_vented_tumble_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/a[2]"
        self.card_pe_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/a"
        self.card_pg_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/a"
        self.card_pk_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/a"
        self.card_dishwasher_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/a[2]"
        self.card_televisions_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/a[2]"
        self.energy_label_fridge_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]"
        self.energy_label_hood_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/a[1]"
        self.energy_label_electric_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/a[1]"
        self.energy_label_gas_oven_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/a[1]"
        self.energy_label_washing_machine_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/a[1]"
        self.energy_label_wine_storage_appliances_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/a[1]"
        self.energy_label_air_vented_tumble_xpath = "/html/body/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/a[1]"
        self.energy_label_dishwasher_xpath = "/html/body/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/a[1]"
        self.energy_label_television_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/a[1]"
        self.energy_label_lamps_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[2]/div[2]/a"
        self.energy_label_tires_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[3]/div[2]/a"
        self.energy_label_heaters_xpath = "/html/body/div/div/div[2]/div[2]/div[4]/div[4]/div[2]/a"
        self.niuch_xpath = "//*[@id='nowaMarka2']/a[4]/button/i"
        self.niuch_source_id = "//*[@id='zr']"
        self.niuch_text_id = "//*[@id='myTextarea']"
        self.niuch_button_xpath = "/html/body/div/div/div[2]/div/button"
        self.cw_button_xpath = "/html/body/div/div[1]/div[1]/div/div/a[2]/button/i"
        self.meta_button_xpath = "/html/body/div/div[1]/div[1]/div/div/a[3]/button/i"
        self.meta_type_input_id = "//*[@id='Rodzaj']"
        self.meta_mark_input_id = "//*[@id='Marka']"
        self.meta_name_input_id = "//*[@id='Nazwa']"
        self.meta_pn_input_id = "//*[@id='Kod']"
        self.meta_button_generator_xpath = "/html/body/div/div/div[2]/div[2]/button"
        self.meta_result_id = "//*[@id='meta_2']"
        self.toys_xpath = "/html/body/div/div[1]/div[2]/div/div/div[5]/div[1]/h4/a"
        self.toys_id_td_xpath = "//*[@id='zabawki']/div/table/tbody/tr/td"
        self.smart_id_td_xpath = "//*[@id='listaMarekSmartfony']/div/table/tbody/tr/td"
        self.rtv_id_td_xpath = "//*[@id='listaMarekRTV']/div/table/tbody/tr/td"
        self.agd_id_td_xpath = "//*[@id='listaMarekAGD']/div/table/tbody/tr/td"


    """ Assert search value from tests
        search_value_temp[0] - tittle of new page
        search_value_temp[1] - search value 
        or 
        svt1  - info about UE directive
    """
    def check_assert(self, search_value):
        cwn = self.driver.current_window_handle
        wn = self.driver.window_handles
        for window in wn:
            if window != cwn:
                self.driver.switch_to.window(window)
                search_value_temp = search_value.split(",")
                self.logger.info("{}".format(search_value_temp[0]))
                self.logger.info("{}".format(search_value_temp[1]))
                assert search_value_temp[0] in self.driver.title, "Wrong tittle"
                svt1 = self.driver.find_elements_by_xpath("//*[contains(text(),'" + search_value_temp[1] + "')]")
                assert len(svt1)>0, "test info"
                self.driver.close()
        self.driver.switch_to.window(cwn)

    """Search AGD plus mark from list in google """
    def agd_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@value='" + args[1] + "']").click()
        search_value_apm = "" + args[2] + ","+ args[0] + " inurl:www." + args[1] + ""
        MainManufacture.check_assert(self, search_value_apm)
        self.driver.find_element_by_xpath(self.field_xpath).clear()
    """
    Search AGD plus all AGD marks in google
    Blocked by capcha
    """
    def agd_plus_mark_full(self, *args):
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        self.driver.implicitly_wait(5)
        le = self.driver.find_elements_by_xpath(self.agd_id_td_xpath) # todo catch radio button
        le_values = [values_le.get_attribute("textContent") for values_le in le]
        for agd_p in le_values:
            if len(agd_p) > 1:
                try:
                    agd_p = agd_p.strip()
                    self.driver.find_element_by_xpath(self.field_xpath).send_keys(agd_p)
                    self.driver.find_element_by_xpath("//input[@value='" + agd_p + "']").click()
                    search_value_apmf = "" + args[0] + "," + agd_p + " inurl:www." + agd_p + ""
                    MainManufacture.check_assert(self, search_value_apmf)
                    self.driver.find_element_by_xpath(self.field_xpath).clear()
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(agd_p))

    """ Open and close new mark on page in google"""
    def new_mark_open_close(self):
        self.driver.find_element_by_xpath(self.no_mark_xpath).click()
        assert self.driver.find_element_by_xpath(self.new_mark_xpath).is_displayed() == True, "No display"
        self.driver.find_element_by_xpath(self.new_mark_close).click()
        assert self.driver.find_element_by_xpath(self.new_mark_xpath).is_displayed() == False, "Still display"


    """Search AGD plus new mark in google"""
    def agd_no_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.no_mark_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.new_mark_xpath).send_keys(args[1])
        self.driver.find_element_by_xpath(self.new_mark_search_xpath).click()
        search_value_anm = "" + args[2] + ","+ args[0] + " inurl:www." + args[1] + ""
        MainManufacture.check_assert(self, search_value_anm)
        self.driver.find_element_by_xpath(self.field_xpath).clear()
        self.driver.find_element_by_xpath(self.new_mark_close).click()

    """Search RTV plus mark from list in google"""
    def rtv_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.RTV_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        rtv_plus_mark_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='" + args[1] + "']")))
        rtv_plus_mark_element.click()
        search_value_rtp = "" + args[2] + ","+ args[0] + " inurl:www." + args[1] + ""
        MainManufacture.check_assert(self, search_value_rtp)
        self.driver.find_element_by_xpath(self.field_xpath).clear()

    """Search smartfon plus mark from list in google"""
    def smart_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        smart_plus_mark_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + args[1] + "']")))
        smart_plus_mark_element.click()
        search_value_spm = "" + args[2] + ","+ args[0] + " inurl:www." + args[1] + ""
        MainManufacture.check_assert(self, search_value_spm)
        self.driver.find_element_by_xpath(self.field_xpath).clear()

    """Search website about smartfons"""
    def smart_portal(self):
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        self.driver.implicitly_wait(5)
        for i in range(3):
            assert_value = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[" + str(
                    i + 6) + "]/td/a").text
            search_value_sm = "" + assert_value + "," + assert_value + ""
            self.driver.find_element_by_xpath(
                "/html/body/div/div[1]/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr[" + str(
                    i + 6) + "]/td/a").click()
            MainManufacture.check_assert(self, search_value_sm)

    """Search toys plus mark from list in google"""
    def toys_plus_mark(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.toys_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        toys_plus_mark_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='" + args[1] + "']")))
        toys_plus_mark_element.click()
        search_value_stm = "" + args[2] + ","+ args[0] + " inurl:www." + args[1] + ""
        MainManufacture.check_assert(self, search_value_stm)
        self.driver.find_element_by_xpath(self.field_xpath).clear()

    """Search pdf in google"""
    def search_pdf(self, *args):
        self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[0])
        self.driver.find_element_by_xpath(self.PDF_xpath).click()
        search_value_sp = "" + args[1] + "," + args[0] + " filetype:pdf"
        MainManufacture.check_assert(self, search_value_sp)
        self.driver.find_element_by_xpath(self.field_xpath).clear()

    """Search EAN or UPS in gs1"""
    def ean_upc(self, *args):
        for i in range(2):
            self.driver.find_element_by_xpath(self.field_xpath).send_keys(args[i])
            self.driver.find_element_by_xpath(self.search_EAN_UPC_xpath).click()
            search_value_eu = "" + args[2] + "," + args[i] + ""
            MainManufacture.check_assert(self, search_value_eu)
            self.driver.find_element_by_xpath(self.field_xpath).clear()

    """Search wrong EAN or UPS """
    def ean_upc_fail(self, fail_v):
        fail_v_len = len(fail_v)
        for i in range(fail_v_len):
            self.driver.find_element_by_xpath(self.field_xpath).send_keys(fail_v[i])
            self.driver.find_element_by_xpath(self.search_EAN_UPC_xpath).click()
            psw = self.driver.switch_to.alert.text
            assert psw == "to nie jest kod EAN", "Bad info"
            self.driver.switch_to.alert.accept()
            self.logger.info("Search value {}".format(fail_v[i]))
            self.driver.find_element_by_xpath(self.field_xpath).clear()

    """open wetransfer """
    def check_wetransfer(self, wetransfer):
        self.driver.find_element_by_xpath(self.link_wetransfer_xpath).click()
        search_value_w = "" + wetransfer + "," + wetransfer + ""
        MainManufacture.check_assert(self, search_value_w)

    """open google translator """
    def check_google_translate(self,google_translate):
        self.driver.find_element_by_xpath(self.link_google_translate_xpath).click()
        search_value_gt = "" + google_translate + "," + google_translate + ""
        MainManufacture.check_assert(self, search_value_gt)

    """open alert with random password"""
    def password_generator(self):
        self.driver.find_element_by_xpath(self.link_password_generator).click()
        psw = self.driver.switch_to.alert.text
        psw_len = len(psw)
        assert psw_len == 10, "Password to short"
        self.logger.info("Password {}".format(psw))
        self.driver.switch_to.alert.accept()

    """open page etykiety"""
    def page_etykiety(self, *args):
        self.driver.find_element_by_xpath(self.button_label_xpath).click()
        search_value_e = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_e)
    """ 
        In etykiety open page with UE card and open label generator in /ec.europa.eu/energy/eepf-labels 
    """
    def energy_label_fridge_card (self, *args):
        self.driver.find_element_by_xpath(self.card_fridge_xpath).click()
        search_value_elfc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elfc)

    def energy_label_hood_card (self, *args):
        self.driver.find_element_by_xpath(self.card_hood_xpath).click()
        search_value_elhc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elhc)

    def energy_label_vacuum_card (self, *args):
        self.driver.find_element_by_xpath(self.card_vacuum_xpath).click()
        search_value_elvc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elvc)

    def energy_label_electric_oven_card(self, *args):
        self.driver.find_element_by_xpath(self.card_electric_oven_xpath).click()
        search_value_eleoc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eleoc)

    def energy_label_gas_oven_card(self, *args):
        self.driver.find_element_by_xpath(self.card_gas_oven_xpath).click()
        search_value_elgoc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elgoc)

    def energy_label_washing_machine_card(self, *args):
        self.driver.find_element_by_xpath(self.card_washing_machine_xpath).click()
        search_value_elwmc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elwmc)

    def energy_label_wine_storage_appliances_card(self, *args):
        self.driver.find_element_by_xpath(self.card_wine_storage_appliances_xpath).click()
        search_value_elwsac = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elwsac)

    def energy_label_air_vented_tumble_card(self, *args):
        self.driver.find_element_by_xpath(self.card_air_vented_tumble_xpath).click()
        search_value_elavtc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elavtc)

    def energy_label_pe_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pe_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_pg_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pg_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_pk_card(self, *args):
        self.driver.find_element_by_xpath(self.card_pk_xpath).click()
        search_value_elpc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_elpc)

    def energy_label_dishwasher_card(self, *args):
        self.driver.find_element_by_xpath(self.card_dishwasher_xpath).click()
        search_value_eldc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eldc)

    def energy_label_television_card(self, *args):
        self.driver.find_element_by_xpath(self.card_televisions_xpath).click()
        search_value_eltc = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_eltc)

    def energy_label_fridge (self, refrigerating):
        self.driver.find_element_by_xpath(self.energy_label_fridge_xpath).click()
        search_value_elf = "" + refrigerating + "," + refrigerating + ""
        MainManufacture.check_assert(self, search_value_elf)

    def energy_label_hood (self, hood):
        self.driver.find_element_by_xpath(self.energy_label_hood_xpath).click()
        search_value_elh = "" + hood + "," + hood + ""
        MainManufacture.check_assert(self, search_value_elh)

    def energy_label_electric_oven(self, electric_oven):
        self.driver.find_element_by_xpath(self.energy_label_electric_oven_xpath).click()
        search_value_eleo = "" + electric_oven + "," + electric_oven + ""
        MainManufacture.check_assert(self, search_value_eleo)

    def energy_label_gas_oven(self, gas_oven):
        self.driver.find_element_by_xpath(self.energy_label_gas_oven_xpath).click()
        search_value_elgo = "" + gas_oven + "," + gas_oven + ""
        MainManufacture.check_assert(self, search_value_elgo)

    def energy_label_washing_machine(self, washing_machine):
        self.driver.find_element_by_xpath(self.card_washing_machine_xpath).click()
        search_value_elwm = "" + washing_machine + "," + washing_machine + ""
        MainManufacture.check_assert(self, search_value_elwm)

    def energy_label_wine_storage_appliances(self, wine):
        self.driver.find_element_by_xpath(self.energy_label_wine_storage_appliances_xpath).click()
        search_value_elwsa = "" + wine + "," + wine + ""
        MainManufacture.check_assert(self, search_value_elwsa)

    def energy_label_air_vented_tumble(self, air_vented_tumble):
        self.driver.find_element_by_xpath(self.energy_label_air_vented_tumble_xpath).click()
        search_value_elavt = "" + air_vented_tumble + "," + air_vented_tumble + ""
        MainManufacture.check_assert(self, search_value_elavt)

    def energy_label_dishwasher(self, dishwasher):
        self.driver.find_element_by_xpath(self.energy_label_dishwasher_xpath).click()
        search_value_eld = "" + dishwasher + "," + dishwasher + ""
        MainManufacture.check_assert(self, search_value_eld)

    def energy_label_television(self, tv):
        self.driver.find_element_by_xpath(self.energy_label_television_xpath).click()
        search_value_elt = "" + tv + "," + tv + ""
        MainManufacture.check_assert(self, search_value_elt)

    def energy_label_lamps(self, lamp):
        self.driver.find_element_by_xpath(self.energy_label_lamps_xpath).click()
        search_value_ell = "" + lamp + "," + lamp + ""
        MainManufacture.check_assert(self, search_value_ell)

    def energy_label_tires(self, tier):
        self.driver.find_element_by_xpath(self.energy_label_tires_xpath).click()
        search_value_elt = "" + tier + "," + tier + ""
        MainManufacture.check_assert(self, search_value_elt)

    def energy_label_heaters(self, heater):
        self.driver.find_element_by_xpath(self.energy_label_heaters_xpath).click()
        search_value_elh = "" + heater + "," + heater + ""
        MainManufacture.check_assert(self, search_value_elh)

    """ 404 """
    def page_cw(self, *args):
        self.driver.find_element_by_xpath(self.cw_button_xpath).click()
        search_value_pcw = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_pcw)

    def page_meta(self, *args):
        self.driver.find_element_by_xpath(self.meta_button_xpath).click()
        search_value_pm = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_pm)

    """ checks the operation of the meta generator, does not check the correctness of the generated meta tags
        does not check all variants of data and incorrect entries
    """

    def page_meta_with_data_without_pn(self, product):
        product_s = product.split()
        self.driver.find_element_by_xpath(self.meta_type_input_id).send_keys(product_s[0])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')]")
        self.driver.find_element_by_xpath(self.meta_mark_input_id).send_keys(product_s[1])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')]")
        self.driver.find_element_by_xpath(self.meta_name_input_id).send_keys(product_s[2])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')][contains(text(),'" + product_s[2] + "')]")

    """ checks the operation of the meta generator, does not check the correctness of the generated meta tags
        does not check all variants of data and incorrect entries
        """
    def page_meta_with_data_with_pn(self, product):
        product_s = product.split()
        self.driver.find_element_by_xpath(self.meta_type_input_id).send_keys(product_s[0])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')]")
        self.driver.find_element_by_xpath(self.meta_mark_input_id).send_keys(product_s[1])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath("//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')]")
        product_s_2 = product_s[2]+" "+product_s[3]+ " "+product_s[4]
        self.driver.find_element_by_xpath(self.meta_name_input_id).send_keys(product_s_2)
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[1] + "')][contains(text(),'" + product_s_2 + "')]")
        self.driver.find_element_by_xpath(self.meta_pn_input_id).send_keys(product_s[5])
        self.driver.find_element_by_xpath(self.meta_button_generator_xpath).click()
        assert self.driver.find_element_by_xpath(
            "//*[contains(text(),'" + product_s[0] + "')][contains(text(),'" + product_s[
                1] + "')][contains(text(),'" + product_s_2 + "')][contains(text(),'" + product_s[5] + "')]")


    def page_niuch(self, *args):
        self.driver.find_element_by_xpath(self.niuch_xpath).click()
        search_value_n = "" + args[0] + "," + args[1] + ""
        MainManufacture.check_assert(self, search_value_n)

    def niuch_with_data(self, *args):
        self.driver.find_element_by_xpath(self.niuch_source_id).send_keys(args[0])
        self.driver.find_element_by_xpath(self.niuch_text_id).send_keys(args[1]+"\n"+args[2]+"\n" +args[3])
        self.driver.find_element_by_xpath(self.niuch_button_xpath).click()
        n_list = []
        cwn_n = self.driver.current_window_handle
        wn_n = self.driver.window_handles
        for window in wn_n:
            if window != cwn_n:
                self.driver.switch_to.window(window)
                nwn_n = self.driver.current_url
                n_list.append(nwn_n)
                self.logger.info("{}".format(nwn_n))
                self.driver.close()
        self.driver.switch_to.window(cwn_n)
        self.logger.info("{}".format(n_list))
        """
        list n_list has inverse values than args
        """
        ar_c = 3
        for i in range(3):
            assert n_list[i] == args[0] + args[ar_c]
            ar_c = ar_c-1

    """In AGD: gets the content of the td element and compares it with its value"""

    """in Name_value comparison in terms of form of writing (case sensitive)"""

    def agd_name_value(self):
        self.driver.find_element_by_xpath(self.AGD_xpath).click()
        le = self.driver.find_elements_by_xpath(self.agd_id_td_xpath) # todo catch radio button
        le_values = [values_le.get_attribute("textContent") for values_le in le]
        for agd_p in le_values:
            if len(agd_p) > 1:
                try:
                    agd_p = agd_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + agd_p + "']").get_attribute("value")
                    assert agd_p == le_temp, "Test fail: no mark "+agd_p+""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(agd_p))

    """In RTV: gets the content of the td element and compares it with its value"""
    def rtv_name_value(self):
        self.driver.find_element_by_xpath(self.RTV_xpath).click()
        lr = self.driver.find_elements_by_xpath(self.rtv_id_td_xpath) # todo catch radio button
        lr_values = [values_lr.get_attribute("textContent") for values_lr in lr]
        for rtv_p in lr_values:
            if len(rtv_p) > 1:
                try:
                    rtv_p = rtv_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + rtv_p + "']").get_attribute("value")
                    assert rtv_p == le_temp, "Test fail: no mark "+rtv_p+""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(rtv_p))

    """In Smart: gets the content of the td element and compares it with its value"""
    def smart_name_value(self):
        self.driver.find_element_by_xpath(self.Smart_xpath).click()
        ls = self.driver.find_elements_by_xpath(self.smart_id_td_xpath)  # todo catch radio button
        ls_values = [values_ls.get_attribute("textContent") for values_ls in ls]
        for smart_p in ls_values:
            if len(smart_p) > 1:
                try:
                    smart_p = smart_p.strip()
                    le_temp = self.driver.find_element_by_xpath("//input[@value='" + smart_p + "']").get_attribute(
                        "value")
                    assert smart_p == le_temp, "Test fail: no mark " + smart_p + ""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format(smart_p))

    """In toys: gets the content of the td element and compares it with its value"""
    # todo page names different from td content (e.g. .com)
    def toys_name_value(self):
        self.driver.find_element_by_xpath(self.toys_xpath).click()
        lt = self.driver.find_elements_by_xpath(self.toys_id_td_xpath)  # todo catch radio button
        lt_values = [values_lt.get_attribute("textContent") for values_lt in lt]
        for toys_p in lt_values:
            if len(toys_p) > 1:
                try:
                    toys_p = toys_p.strip()
                    lt_temp = self.driver.find_element_by_xpath("//input[@value='" + toys_p + "']").get_attribute(
                    "value")
                    assert toys_p == lt_temp, "Test fail: no mark " + toys_p + ""
                except NoSuchElementException:
                    self.logger.info("FAIL IN {}".format (toys_p))