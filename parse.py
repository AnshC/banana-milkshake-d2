import csv
import os
import argparse


def read_csv(file_path, output_file):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader) 

        meet_name  = data[0][0]
        meet_date = data[1][0]
        meet_link = data[2][0]
        meet_summary = ""
        team_results_string = "<table><tr><th>Position</th><th>Team</th><th>Score</th></tr>"
        athelete_result_string = "<table><tr><th>Place</th><th>Grade</th><th>Name</th><th>Time</th><th>Team</th></tr>"
        photo_gallery = "<table><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><tr>"
        current_row = 0

        for i in range (0, len(data[3])):
            meet_summary = meet_summary + (data[3][i])

        # parse team results
        for row in range(7, len(data)):
            if not data[row]:
                team_results_string = team_results_string + "</table>"
                current_row = row
                break
            place_string = data[row][0]
            team_string = data[row][1]
            score_string = data[row][2]
            team_results_string = team_results_string + f"<tr><td>{place_string}</td><td>{team_string}</td><td>{score_string}</td></tr>"

        temp = 0

        # parse athlete results
        for row in range(current_row + 2, len(data)):
            place_string = data[row][0]
            grade_string = data[row][1]
            name_string = data[row][2]
            athlete_link_string = data[row][3]
            time_string = data[row][4]
            team_string = data[row][5]

            # team_link_string = data[row][6]
            alt_string = name_string + "Running"
            profile_string = "AthleteImages/" + data[row][7]

            if (temp > 0 and temp%5 == 0):
                photo_gallery = photo_gallery + f"</tr><tr>"

            else:
                photo_gallery = photo_gallery + f"<td><img src={profile_string} alt={name_string} width='100'></td>"
            temp += 1

            athelete_result_string = athelete_result_string + f"<tr><td>{place_string}</td><td>{grade_string}</td><td><div class='athlete-profile'><img width = '100' src='{profile_string}' alt={alt_string}>{name_string}<a href='{athlete_link_string}'>Profile link</a></div></td><td>{time_string}</td><td>{team_string}</td></tr>"

        athelete_result_string = athelete_result_string + "</table>"
        photo_gallery = photo_gallery + "</tr></table>"

        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meet_name}</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <h2>{meet_date}</h2>
        <a href="{meet_link}">Learn more about this event!</a>
        <p>{meet_summary}</p>


        <nav>
            <ul>
                <li><a href="#team-results">Team Results</a></li>
                <li><a href="#athlete-results">Athlete Results</a></li>
                <li><a href="#gallery">Gallery</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="team-results">
            <h2>Team Results</h2>
            {team_results_string}
        </section>

        <section id="athlete-results">
            <h2>Athlete Results</h2>
            {athelete_result_string}
        </section>

        <section id="gallery">
            <h2>Photo Gallery</h2>
            {photo_gallery}
        </section>
    </main>

    <footer>
        <p>&copy; BANANA MILKSHAKE. All rights reserved.</p>
    </footer>
</body>
</html>
        """

        with open(output_file, 'w') as ofile:
            ofile.write(html_content)


def main():

    # File Locations
    default_meet_file = "37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv"
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "meet_file",
        nargs="?",
        default=default_meet_file,
        help="The meet file name end with .csv",
    )

    args = parser.parse_args()
    meet_file = args.meet_file

    path = "meets/"
    output_file = meet_file.rstrip(".csv") + ".html"
    read_csv(path + meet_file, output_file)

if __name__ == "__main__":
    main()
