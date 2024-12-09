import sys
import time
from iau import iau
from wapp import wapp


group_name = "COMPUTER PROGRAMMING- HOMEWORK"
admin_name = "A5CT Admin"

driver = iau.open_driver()

if driver == 1:
    wapp.send_msg(admin_name, "Error while opening driver.")
    sys.exit("Error while opening driver.")


lesson_announcement_error_check = True
notes_error_check = True
homeworks_error_check = True
results_error_check = True

time.sleep(15)
while True:
    lesson_announcement = iau.check_lesson_announcement(driver)
    if isinstance(lesson_announcement, str):
        wapp.send_msg(group_name, lesson_announcement)
    elif lesson_announcement == 1 and lesson_announcement_error_check:
        wapp.send_msg(admin_name, "Error while getting lesson announcement.")
        lesson_announcement_error_check = False

    time.sleep(15)
    notes = iau.check_notes(driver)
    if isinstance(notes, str):
        wapp.send_msg(group_name, notes)
    elif notes == 1 and notes_error_check:
        wapp.send_msg(admin_name, "Error while getting notes.")
        notes_error_check = False

    time.sleep(15)
    homeworks = iau.check_homeworks(driver)
    if isinstance(homeworks, str):
        wapp.send_msg(group_name, homeworks)
    elif homeworks == 1 and homeworks_error_check:
        wapp.send_msg(admin_name, "Error while getting homeworks.")
        homeworks_error_check = False

    time.sleep(15)
    results = iau.check_results(driver)
    if isinstance(results, str):
        wapp.send_msg(group_name, results)
    elif results == 1 and results_error_check:
        wapp.send_msg(admin_name, "Error while getting exam results.")
        results_error_check = False

    time.sleep(15)
    working = iau.check_working(driver)
    if isinstance(working, str):
        wapp.send_msg(admin_name, working)

    time.sleep(100)

driver.quit()
