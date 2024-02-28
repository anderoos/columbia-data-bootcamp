import csv 
import time


def analyze_poll_results(dict_data):
    # Count num votes casted
    total_num_votes_cast = len(list(dict_data))
    # Store header labels
    col_labels = list(dict_data)[0].keys()
    # Retrieve votes and put into empty list
    all_votes_list = []
    for row in dict_data:
        all_votes_list.append(row['Candidate'])
    # Convert list to set, then back to list to get unique values
    candidate_who_recd_votes_set = set(all_votes_list)
    list_of_candidates = list(candidate_who_recd_votes_set)
    # Count votes per candidate and assign to dict results_abs
    results_abs = {}
    for candidate in list_of_candidates:
        results_abs[candidate] = all_votes_list.count(candidate)
    # Calculate percentages and assign to dict results_as_percentages using absolute values in results_abs
    results_as_percentages = {}
    for candidate, votes in results_abs.items():
        results_as_percentages[candidate] = round((votes/total_num_votes_cast)* 100, 3)
    # Get the highest % and capture it in winner_percentage
    winner_percentage = max(results_as_percentages.values())
    # Use the % to find which candidiate it was and assign it to winner
    winner = [candidate for candidate, percentage in results_as_percentages.items() if percentage == winner_percentage]
    print(f"""
        Election Results
        -------------------------
        Total Votes: {total_num_votes_cast}
        -------------------------
        {list_of_candidates[0]} : {results_as_percentages[list_of_candidates[0]]}% with {results_abs[list_of_candidates[0]]} votes.
        {list_of_candidates[1]} : {results_as_percentages[list_of_candidates[1]]}% with {results_abs[list_of_candidates[1]]} votes.
        {list_of_candidates[2]} : {results_as_percentages[list_of_candidates[2]]}% with {results_abs[list_of_candidates[2]]} votes.
        -------------------------
        Winner: {winner[0]} : {winner_percentage}
        -------------------------
        """)
    # Export as txt
    export_status = input("Export file as .txt? ")
    if export_status == "Yes":
        print("Exporting...\n")
        time.sleep(1)
        with open('Pypoll/analysis/results.txt', "w") as export:
            export.write(f"""
            Election Results
            -------------------------
            Total Votes: {total_num_votes_cast}
            -------------------------
            {list_of_candidates[0]} : {results_as_percentages[list_of_candidates[0]]}% with {results_abs[list_of_candidates[0]]} votes.
            {list_of_candidates[1]} : {results_as_percentages[list_of_candidates[1]]}% with {results_abs[list_of_candidates[1]]} votes.
            {list_of_candidates[2]} : {results_as_percentages[list_of_candidates[2]]}% with {results_abs[list_of_candidates[2]]} votes.
            -------------------------
            Winner: {winner[0]} : with {winner_percentage}% of votes.
            -------------------------
            """)

# Execute function:
with open("Pypoll/Resources/election_data.csv", newline="") as election_data:
    election_data_dict = list(csv.DictReader(election_data, delimiter=","))
    analyze_poll_results(election_data_dict)