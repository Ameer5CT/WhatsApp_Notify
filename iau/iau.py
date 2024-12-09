import os
import time
from selenium.webdriver.common.by import By
from seleniumbase import Driver

saved_lesson_announcement = ""
saved_notes = ""
saved_notes_list = []
saved_homeworks = ""
saved_homeworks_list = []
saved_results = ""
saved_results_list = []
saved_working = ""


def open_driver():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        profile_dir = os.path.join(current_dir, "iau_profile")

        driver = Driver(uc=True, user_data_dir=profile_dir)
        driver.uc_open_with_reconnect("https://ubis.aydin.edu.tr/?Pointer=Main&ucLang=TR", 4)
        driver.uc_gui_click_captcha()

        driver.set_window_size(300, 300)
        driver.set_window_position(-2000, 0)
        # driver.minimize_window()
        return driver
    except:
        return 1


def check_lesson_announcement(driver):
    try:
        driver.get("https://ubis.aydin.edu.tr/?Pointer=Main&ucLang=TR")
        time.sleep(5)
        lesson_announcement = driver.find_element(By.ID, "content-2").find_element(By.ID, "lnews_0")
        global saved_lesson_announcement

        if saved_lesson_announcement == "":
            saved_lesson_announcement = lesson_announcement.text
            # Return no announcement and no error
            return 0

        if lesson_announcement.text != saved_lesson_announcement:
            saved_lesson_announcement = lesson_announcement.text
            temp_list = []
            for i in lesson_announcement.find_elements(By.TAG_NAME, "td"):
                temp_list.append(i.text)
            lesson_announcement.find_element(By.TAG_NAME, "a").click()
            time.sleep(5)
            details = driver.find_element(By.ID, "cContent")
            writer_txt = details.find_element(By.CLASS_NAME, "r").text
            temp_list.append(details.text.replace(writer_txt, "").strip())
            text = ("!!! Lesson Announcement !!!\n"
                    "=========================\n" +
                    temp_list[1] + "\n" +
                    temp_list[2] + "\n\n" +
                    temp_list[3] + "\n" +
                    temp_list[5])
            # Return the new announcement
            return text
        else:
            # Return no announcement and no error
            return 0
    except:
        # Return error
        return 1


def check_notes(driver):
    try:
        driver.get("https://ubis.aydin.edu.tr/?Pointer=Ogrenci&Page=DersNotlarim&")
        time.sleep(5)
        notes = driver.find_element(By.ID, "cContent").find_element(By.TAG_NAME, "tbody")
        global saved_notes, saved_notes_list

        if saved_notes == "":
            saved_notes = notes.text
            temp_list = []
            count = 0
            for i in notes.find_elements(By.TAG_NAME, "tr"):
                temp_list.append(["x"])
                for j in i.find_elements(By.TAG_NAME, "td"):
                    temp_list[count].append(j.text)
                count += 1

            notes_list = [row[-1] for row in temp_list]
            saved_notes_list = notes_list

            # Return no error
            return 0

        if notes.text != saved_notes:
            saved_notes = notes.text

            temp_list = []
            count = 0
            for i in notes.find_elements(By.TAG_NAME, "tr"):
                temp_list.append(["x"])
                for j in i.find_elements(By.TAG_NAME, "td"):
                    temp_list[count].append(j.text)
                if temp_list[-1][-1] != saved_notes_list[count]:
                    saved_notes_list[count] = temp_list[-1][-1]
                    i.click()
                    time.sleep(5)

                    notes_des = driver.find_element(By.ID, "cContent").find_element(By.TAG_NAME, "tbody")
                    trs = notes_des.find_elements(By.TAG_NAME, "tr")
                    for k in trs[1].find_elements(By.TAG_NAME, "td"):
                        temp_list[-1].append(k.text)

                    text = ("!!! Course Note !!!\n"
                            "=========================\n" +
                            temp_list[-1][2] + "\n" +
                            temp_list[-1][3] + "\n\n" +
                            temp_list[-1][8] + "\n" +
                            temp_list[-1][9])
                    return text

                count += 1
        else:
            # Return no error
            return 0
    except:
        # Return error
        return 1


def check_homeworks(driver):
    try:
        driver.get("https://ubis.aydin.edu.tr/?Pointer=Ogrenci&Page=Odevler&")
        time.sleep(5)
        homeworks = driver.find_element(By.ID, "cContent").find_element(By.TAG_NAME, "tbody")
        global saved_homeworks, saved_homeworks_list

        if saved_homeworks == "":
            saved_homeworks = homeworks.text
            temp_list = []
            count = 0
            for i in homeworks.find_elements(By.TAG_NAME, "tr"):
                temp_list.append(["x"])
                for j in i.find_elements(By.TAG_NAME, "td"):
                    temp_list[count].append(j.text)
                count += 1

            homeworks_list = [row[-1] for row in temp_list]
            saved_homeworks_list = homeworks_list

            # Return no error
            return 0

        if homeworks.text != saved_homeworks:
            saved_homeworks = homeworks.text

            temp_list = []
            count = 0
            for i in homeworks.find_elements(By.TAG_NAME, "tr"):
                temp_list.append(["x"])
                for j in i.find_elements(By.TAG_NAME, "td"):
                    temp_list[count].append(j.text)
                if temp_list[-1][-1] != saved_homeworks_list[count]:
                    saved_homeworks_list[count] = temp_list[-1][-1]
                    i.click()
                    time.sleep(5)

                    homeworks_des = driver.find_element(By.ID, "cContent").find_element(By.TAG_NAME, "tbody")
                    trs = homeworks_des.find_elements(By.TAG_NAME, "tr")
                    for k in trs[1].find_elements(By.TAG_NAME, "td"):
                        temp_list[-1].append(k.text)

                    text = ("!!! Homework !!!\n"
                            "=========================\n" +
                            temp_list[-1][1] + "\n" +
                            temp_list[-1][2] + "\n\n" +
                            temp_list[-1][6] + "\n" +
                            temp_list[-1][8])
                    return text

                count += 1
        else:
            # Return no error
            return 0
    except:
        # Return error
        return 1


def check_results(driver):
    try:
        driver.get("https://ubis.aydin.edu.tr/?Pointer=Ogrenci&Page=SinavSonuclarim&")
        time.sleep(5)
        results = driver.find_element(By.ID, "cContent").find_elements(By.TAG_NAME, "tbody")[1]
        global saved_results, saved_results_list

        if saved_results == "":
            saved_results = results.text

            temp_list = []
            count = 0
            for i in results.find_elements(By.TAG_NAME, "tr"):
                if count % 2 == 1:
                    temp_list.append(i.text)
                count += 1

            saved_results_list = temp_list

            # Return no error
            return 0

        if results.text != saved_results:
            saved_results = results.text

            temp_list = []
            count = 0
            all_rows = results.find_elements(By.TAG_NAME, "tr")
            for i in all_rows:
                if count % 2 == 1:
                    temp_list.append(i.text)
                count += 1

            temp_list2 = []

            for i in range(len(temp_list)):
                if temp_list[i] != saved_results_list[i]:
                    saved_results_list[i] = temp_list[i]

                    lec_name = all_rows[(i * 2)].find_element(By.TAG_NAME, "th").text
                    temp_list2.append(lec_name.split()[0])
                    temp_list2.append(lec_name.split(' ', 1)[1])

                    lec_result = all_rows[ ( (i*2) + 1 )].find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")
                    temp_list2.append(lec_result[0].text)
                    temp_list2.append(lec_result[1].text)

                    text = ("!!! Exam Result !!!\n"
                            "=========================\n" +
                            temp_list2[0] + "\n" +
                            temp_list2[1] + "\n\n" +
                            temp_list2[2] + "     " + temp_list2[3])
                    return text
        else:
            # Return no error
            return 0
    except:
        # Return error
        return 1


def check_working(driver):
    try:
        driver.get("https://ubis.aydin.edu.tr/?Pointer=KGS&Page=GirisCikisBilgilerim&")
        time.sleep(5)
        working = driver.find_element(By.ID, "cContent").text
        global saved_working

        if working != saved_working:
            saved_working = working

            return "The bot is working."
        else:
            # Return no error
            return 0
    except:
        # Return error
        return "The bot is NOT working."
