import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DICT = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}

def get_user_input(check_data, message, error_message):
    while True:
        user_input = input(message).lower()
        if user_input not in check_data:
            print(error_message)
            print("Please Try again")
            continue
        else:
            break
    return user_input
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = ''
    month = ''
    day = ''
    
    # To be used for better code readability 
    user_message_data = {"city":[{"message": "Which city you want to check data for, please select from chicago, new york city, or washington?\n",
                                 "error_message": "\nWRONG INPUT FOR CITY, please only select from chicago, new york city, or washington",
                                 "data": ['chicago','new york city','washington']}],
                        "month":[{'message': "Which month you want to check data for, please select between January to June or select all to data for all months?\n",
                                 "error_message": "\nWRONG INPUT FOR Month, please only select from January to June or select 'all'",
                                 "data": ['january', 'february', 'march', 'april', 'may', 'june','all']}],
                        "weekday":[{"message": "Which weekday you want to check data for, please select between Monday to Sunday or select all to data for all days?\n",
                                 "error_message": "\nWRONG INPUT FOR Day, please only select from Monday to Sunday or select 'all'",
                                 "data": ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']}]}
    #iterating over dict here
    for key in user_message_data.keys():
        data = user_message_data[key][0]
        if key == "city":
            city = get_user_input(data["data"], data["message"], data["error_message"])
        elif key == "month":
            month = get_user_input(data["data"], data["message"], data["error_message"])
        elif key == "weekday":
            day = get_user_input(data["data"], data["message"], data["error_message"])    
            
    
    print('-'*40)
    
    return city, month, day


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
    print(f"Reading Data for {city} city")
    
    df = pd.read_csv(CITY_DATA[city])
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day_name()
    print(df['month'])
    print(df['weekday'])
    # Month filter
    if month != "all":
        month_number = list(MONTH_DICT.keys())[list(MONTH_DICT.values()).index(month)]
        df = df[df['month'] == month_number]
    # Day fiter
    if day != "all":
        df = df[df['weekday'] == day.title()]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df['month'].mode())
    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]
    print("Most frequent Month is: ",MONTH_DICT[most_freq_month])
    
    # TO DO: display the most common day of week
    most_freq_weekday = df['weekday'].mode()[0]
    print("\nMost frequent Week is: ", most_freq_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_freq_weekday = df['hour'].mode()[0]
    print("\nMost frequent Hour is: ", most_freq_weekday)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", most_common_start_station)    

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("\nMost commonly used end station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station']+' | '+df['End Station']
    most_common_start_end_station = df['Start_End Station'].mode()[0]
    print('\nMost frequent combination of start station and end station trip: ', most_common_start_end_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_travel_time = df['Trip Duration'].sum()
        print(f"Total travel time: {total_travel_time} seconds")
    except:
        print("Column named Trip Duration not in the dataset")
        
    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    print(f"\nMean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print("\nCount of user types:\n",df['User Type'].value_counts())
    except:
        print("\nColumn name 'User Type' not present in dataset")
        
    # TO DO: Display counts of gender
    try:
        print("\nCount of gender:\n",df['Gender'].value_counts())
    except:
        print("\nColumn name 'Gender' not present in dataset")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("\nEarliest year of birth is: ", df['Birth Year'].min())
        print("Most Recent year of birth is: ", df['Birth Year'].max())
        print("Most common year of birth is: ", df['Birth Year'].mode()[0])
    except:
        print("\nColumn name Birth year is not present in dataset")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
<<<<<<< HEAD
<<<<<<< HEAD
    """Function to display raw data to user. This function is displaying 5 rows of the sample dataframe."""
=======
    """Function to display raw data to user. it will display first five rows of the dataframe for each city."""
>>>>>>> refactoring
=======
    """Function to display raw data to user. it will display first five rows of the dataframe for each city."""
=======
    """Function to display raw data to user. This function is displaying 5 rows of the sample dataframe."""
>>>>>>> documentation
>>>>>>> refactoring
    while True:
        disp_data_input = input("Do you wish to see first five row sample of the data? Please input yes or no!\n").lower()
        
        if disp_data_input == 'no':
            return print("Thank you! The data will not be displayed")
        
        elif disp_data_input == 'yes':
            row_num = 5
            print(df.iloc[0:row_num])
            while True:
                
                continue_show = input("Want to see more data type yes to continue or no to stop\n").lower()
                if continue_show == 'yes':
                    print(row_num,"\n")
                    print(df.iloc[row_num:row_num+5])
                    row_num += 5
                    continue
                else:
                    return print("No more data will be displayed")
                
        else:
            print("Please enter a valid input (yes/no) you cannot use y/n ")
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
"""calls the main function"""
    main()
