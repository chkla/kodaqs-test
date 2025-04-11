
# 📘 Codebook: 2017 German Federal Election Dataset

This dataset contains aggregated results of the 2017 German federal election by electoral district (Wahlkreis).

Source: https://www.govdata.de/suche/daten/bundestagswahl-2017

## 📄 General Information

- **Rows**: 299 (One per electoral district)
- **Columns**: 10
- **Source**: German Federal Returning Officer (Bundeswahlleiter)

---

## 📚 Variables

| Column Name              | Description                                                                 | Type    | Example                          |
|--------------------------|-----------------------------------------------------------------------------|---------|----------------------------------|
| `Unnamed: 0`             | Index column, likely redundant (row number).                                | int     | 1                                |
| `area_id`                | Unique ID for each electoral district.                                      | int     | 1                                |
| `area_names`             | Name of the electoral district.                                             | string  | Flensburg – Schleswig            |
| `state`                  | Name of the federal state (Bundesland) to which the district belongs.       | string  | Schleswig-Holstein              |
| `registered.voters`      | Number of voters registered in the district.                                | int     | 225,659                          |
| `total_votes`            | Total number of ballots cast (including invalid votes).                     | int     | 171,905                          |
| `invalid_first_votes`    | Number of invalid *first votes* (Erststimme).                               | int     | 1,647                            |
| `invalid_second_votes`   | Number of invalid *second votes* (Zweitstimme).                             | int     | 1,509                            |
| `valid_first_votes`      | Number of valid *first votes* cast in the district.                         | int     | 170,258                          |
| `valid_second_votes`     | Number of valid *second votes* cast in the district.                        | int     | 170,396                          |

---

## 🗳️ Notes

- **First Vote (Erststimme)**: Elects a local representative via first-past-the-post voting.
- **Second Vote (Zweitstimme)**: Determines the proportional representation of parties in the Bundestag.
- Invalid votes are included in `total_votes` but excluded from `valid_*` columns.
