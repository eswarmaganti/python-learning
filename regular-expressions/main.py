import re

# Extract Phone Number
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
# declaring a regular expression pattern using raw string
pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
matches = re.findall(pattern, text)
print("Phone Numbers: ", matches)


# Extract Note Titles
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern = r'Note \d - ([^\n]*)'
matches = re.findall(pattern, text)
print("Titles: ", matches)


# Extract financial periods from companies accounting information

# case-sensitive
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. In quarter fy2021 Q2 was $ billion.
'''

pattern = r'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text)
print("Financial periods: ", matches)

# case-insensitive
pattern = r'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text,flags=re.IGNORECASE)
print("Financial periods: ", matches)


# Extract only financial numbers
pattern = r'\$[^ ]+'
matches = re.findall(pattern, text)
print("Financial Information: ", matches)


# Extract Financial periods and numbers both

pattern= r'FY(\d{4} Q[1-4]) [^\$]+(\$[^ ]+)'
matches = re.findall(pattern, text)
print("Financial Information: ", matches)

# using search method
match = re.search(pattern,text)
print("First Match: ", match.groups())
print(f"First Match start-position: {match.start()} end-position: {match.end()}")


# the split method
text = "My Name is Eswar Krishna Maganti"
print("Split the data based on a pattern: ", re.split("\s", text))
print("Limit the splits", re.split("\s", text, 2))


# The sub method is used to replace the matched patterns
print(re.sub(r"E.*r ","eswar ", text))


