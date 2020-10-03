import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list=['january', 'february', 'march', 'april', 'may', 'june']
day_list=["friday","saturday","sunday","monday","tuesday","wednesday","thursday"]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_selection = input('To view the available bikeshare data, kindly type:\n(c) for Chicago\n(n) for New York City\n(w) for Washington\n  ').lower()
    while city_selection not in {"c","n","w"}:
        print('Please Eneter a valid Character for city selection: c,n or w\n')
        city_selection = input('To view the available bikeshare data, kindly type:\n(c) for Chicago\n(n) for New York City\n(w) for Washington\n  ').lower()
    if city_selection=="c":
        city="chicago"
    elif city_selection=="n":
        city="new york city"
    elif city_selection=="w":
        city="washington"
# TO DO: get user input for month (all, january, february, ... , june)
    time_frame = input('\n\n Would you like to filter {}\'s data by month, day, both, or not at all?\n type month or day or both or none: \n'.format(city.title())).lower()
    while time_frame not in {"month","day","both","none"}:

        print("Please enter a valid choice!")
        time_frame = input('\n\n Would you like to filter {}\'s data by month, day, both, or not at all?\n type month or day or both or none: \n'.format(city.title())).lower()
   
    if time_frame=="none":
        print('\n Filtering for {} for the 6 months period \n'.format(city.title()))
        month="all"
        day="all"
    elif time_frame=="both":
                #Collecting user input for month name
        month_selection = input("Please write the month name required for filter\n Available Months: January/February/March/April/May/June\n").lower()
        while month_selection not in month_list:
            print("\n Please write a valid month name\n")
            month_selection = input("Please write the month name required for filter\n Available Months: January/February/March/April/May/June\n").lower()
        
        month=month_selection
        #Collecting user input for day name
        day_selection = input("Please write the week day name required for filter\nExample: Friday/Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday\n").lower()
        while day_selection not in day_list:
            print("\n Please write a valid day name\n")
            day_selection = input("Please write the week day name required for filter\nExample: Friday/Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday\n").lower()
        day=day_selection
        print('\n Filtering for {} for {} month and {} week day \n'.format(city.title(),month.title(),day.title()))
    #Input for month only filter
    elif time_frame=="month":
        month_selection = input("Please write the month name required for filter\n Available Months: January/February/March/April/May/June\n").lower()
        while month_selection not in month_list:
            print("\n Please write a valid month name\n")
            month_selection = input("Please write the month name required for filter\n Available Months: January/February/March/April/May/June\n").lower()
        
        month=month_selection
        day="all"
        print('\n Filtering for {} for {} month and {} week days \n'.format(city.title(),month.title(),day.title()))
    #Input for day only filter
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif time_frame=="day":
        day_selection = input("Please write the week day name required for filter\nExample: Friday/Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday\n").lower()
        while day_selection not in day_list:
            print("\n Please write a valid day name\n")
            day_selection = input("Please write the week day name required for filter\nExample: Friday/Saturday/Sunday/Monday/Tuesday/Wednesday/Thursday\n").lower()
        day=day_selection
        month="all"
        print('\n Filtering for {} for {} months and {} week day \n'.format(city.title(),month.title(),day.title()))
    print('-'*40)
    return (city,month,day)

filtered_values = get_filters()
city, month, day = filtered_values

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
    
        month = month_list.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
load_data(city,month,day)
df=load_data(city,month,day)

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month as number
    cm = df['month'].mode()[0]
    #retrieve month name from month_list
    common_month= month_list[cm-1].title()  
    print('Most Common Starting Month:{}'.format(common_month))    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Starting day of week:', common_day)
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular starting hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(df,month,day)   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df["Start Station"].mode()[0]
    print('Most commonly used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station=df["End Station"].mode()[0]
    print('Most commonly used ending station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip"]=df["Start Station"]+"-"+df["End Station"]
    most_trip=df["Trip"].mode()[0]
    count_c=df["Trip"].nunique()
 
    print('Most frequent combination of start station and end station trip:\n Start Station         -     End Station\n', most_trip)
    print("\nCommon Trip Unique Count: {} ".format(count_c))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(df)    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_duration = float(str(df["Trip Duration"].sum()))
    days = travel_duration // (24 * 3600)
    travel_duration= travel_duration % (24 * 3600)
    hour = travel_duration // 3600
    travel_duration %= 3600
    minutes = travel_duration // 60
    travel_duration %= 60
    seconds = travel_duration
    print("Total Traveling Time: d:h:m:s-> %d:%d:%d:%d" % (days, hour, minutes, seconds))
    
    # TO DO: display mean travel time
    average_travel_duration = float(str(df["Trip Duration"].mean()))
    days = average_travel_duration // (24 * 3600)
    average_travel_duration= average_travel_duration % (24 * 3600)
    hour = average_travel_duration // 3600
    average_travel_duration %= 3600
    minutes = average_travel_duration // 60
    average_travel_duration %= 60
    seconds = average_travel_duration
    print("Average Traveling Time: d:h:m:s-> %d:%d:%d:%d" % (days, hour, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User Types Count:')
    # TO DO: Display counts of user types
    user_type=df["User Type"].value_counts()
    print("{}\n".format(user_type))
    # TO DO: Display counts of gender
    if  "Gender" and "Birth Year" not in df.columns:      
        print("\nSorry,No Gender or Birth Year info available for Washington dataset!")
    else:
        print('User Gender Count:')
        gender_count=df["Gender"].value_counts()
       
        print("{}\n".format(gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest=df["Birth Year"].min()
        recent=df["Birth Year"].max()
        common_year=df["Birth Year"].mode()[0]
        print("Detecting Earlest,Most Recent and Common Birth Year ....")        
        print("\n Earliest Birth Year : {}\n Most Recent Birth Year: {}\n Most Common Birth Year: {}\n".format(int(earliest),int(recent),int(common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
user_stats(df)

def display_raw_data(city):
    
        """Asking User if will be interested in exploring chunks of raw data"""
        display_raw = input("Would you like to have a look on the raw data? Type yes or no\n").lower()
        while display_raw == 'yes':
            try:
                for chunk in pd.read_csv(CITY_DATA.get(city), chunksize=5):
                    print(chunk)
                    # repeating the question
                    display_raw = input("Would you like to explore more raw data? Type yes or no\n").lower()
                    if display_raw != 'yes':
                        print('Thank You!')
                        break
                break        
            except KeyboardInterrupt:
                print('Thank you!')
display_raw_data(city)

def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)




if __name__ == "__main__":
	main()

