import csv

# File Locations
path = 'meets/'
meet_file = '37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv'
output_file = meet_file.rstrip('.csv') + '.html'

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader) 

        meet_name  = data[0][0]
        meet_date = data[1][0]
        meet_link = data[2][0]
        meet_summary = ""
        team_results_string = "<table><tr><th>Position</th><th>Team</th><th>Score</th></tr>"
        athelete_result_string = "<table><tr><th>Place</th><th>Grade</th><th>Name</th><th>Time<th>Team</th></th></tr>"
        current_row = 0

        for i in range (0, len(data[3])):
            meet_summary = meet_summary + (data[3][i])

        #parse team results
        for row in range(7, len(data)):
            if not data[row]:
                team_results_string = team_results_string + "</table>"
                current_row = row
                break
            place_string = data[row][0]
            team_string = data[row][1]
            score_string = data[row][2]
            team_results_string = team_results_string + f"<tr><td>{place_string}</td><td>{team_string}</td><td>{score_string}</td></tr>"
        
        #parse athlete results
        for row in range(current_row + 2,len(data)):
            if not data[row]:
                athelete_result_string = athelete_result_string + "</table>"
                break
            place_string = data[row][0]
            grade_string = data[row][1]
            name_string = data[row][2]
            athlete_link_string = data[row][3]
            time_string = data[row][4]
            team_string = data[row][5]
            team_link_string = data[row][6]
            profile_string = "AthleteImages/" + data[row][7]
            
            athelete_result_string = athelete_result_string + f"<tr><td>{place_string}</td><td>{grade_string}</td><td><div><img width = '100px' src='{profile_string}'alt={name_string}>{name_string}<a href='{athlete_link_string}'>Profile link</a></div></td><td>{time_string}</td><td>{team_string}<a href='{team_link_string}'</a></td></tr>"
            
        

        html_content = f'''
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
        <a href="{meet_link}">Link</a>
        <p>Description: {meet_summary}</p>


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
            <p>TODO</p>
        </section>
    </main>

    <footer>
    THIS IS FOOTER!
    </footer>
</body>
</html>
        '''

        with open(output_file, 'w') as ofile:
            ofile.write(html_content)

        

read_csv(path + meet_file)