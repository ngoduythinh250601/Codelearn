def validPhoneNumber(phone):
    invalid = ["4", "7", "0"]
    return (
        len(phone) == 10
        and phone.isdigit()
        and phone[0] == "0"
        and phone[-1] not in invalid
    )
