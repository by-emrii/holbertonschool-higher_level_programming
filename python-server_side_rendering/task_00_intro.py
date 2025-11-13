import os


def generate_invitations(template, attendees):
    # check input types
    if not isinstance(template, str):
        print("Error: template should be type string.")
        return
    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        print("Error: attendees should be a list of dictionaries.")
        return

    # handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # create a copy of each attendee
        invitation_text = template[:]

        # replace placeholders and N/A if key is empty or None
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))

        # write to output file
        filename = f"output_{index}.txt"
        try:
            # avoid over writing if the file already exists
            if os.path.exists(filename):
                os.remove(filename)

            with open(filename, "w", encoding="utf-8") as f:
                f.write(invitation_text)

            print(f"{filename} generated")
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
