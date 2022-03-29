import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Would you like to see data for Chicago, new york city, or Washington? \n").lower()
    while city not in CITY_DATA:
        print('invalid inputs')
        print()
        city = input("Please Choose From this list : Chicago, new york city, or Washington \n").lower()   

    data_filter = input("Would you like to filter the data by month, day,both,or none? \n").lower()
    data_filter_choose = ['month', 'day','both','none']
    while data_filter not in data_filter_choose:
        print('invalid inputs')
        print()
        data_filter = input("Please Choose From this list : month,day,both,none \n").lower()
    
    
    if data_filter == 'month':
    # TO DO: get user input for month (all, january, february, ... , june)
        month = input("(If they chose month) Which month - January, February, March, April, May, or June? \n").lower()
        day = 'all'        
    elif data_filter == 'day':
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n").lower()
        month = 'all'
    elif data_filter == 'both':
        month = input("(If they chose month) Which month - January, February, March, April, May, or June? \n").lower()
        day = input("(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n").lower()
    else:
        month = 'all'
        day = 'all'

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
    try : 
        df = pd.read_csv(CITY_DATA[city])
   
        df['Start Time'] = pd.to_datetime(df['Start Time'] )

        df['month'] = df['Start Time'].dt.month

        df['day_of_week'] = df['Start Time'].dt.weekday_name



        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]
            
        if day != 'all':
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
            days.index(day) 
            df = df[df['day_of_week'] == day.title()]

    except (KeyError,ValueError):
         print("you entered wrong city or month or day ")
         df = pd.DataFrame()
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if len(df['month'].unique()) > 1 :
        popular_month =  df['month'].value_counts().idxmax()
        n_popular_month = df['month'].value_counts().max()
        print('Most Frequent Start month:',popular_month)
        print('\tnumber of month:',n_popular_month)
        print()
    else:
        print('Data is filltered by month')
        print()
        
    # TO DO: display the most common day of week
    if len(df['day_of_week'].unique()) > 1 :
        popular_day =  df['day_of_week'].value_counts().idxmax()
        n_popular_day = df['day_of_week'].value_counts().max()
        print('Most Frequent Start day of week:',popular_day)
        print('\tnumber of day:',n_popular_day)
        print()
    else:
        print('Data is filltered by day')
        print()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour =  df['hour'].value_counts().idxmax()
    n_popular_hour = df['hour'].value_counts().max()
    print('Most Frequent Start hour:',popular_hour)
    print('\tnumber of hour:',n_popular_hour)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station =  df['Start Station'].value_counts().idxmax()
    n_popular_start_station =  df['Start Station'].value_counts().max()
    print('Most Frequent Start Station:',popular_start_station)
    print('\tnumber of Start Station:',n_popular_start_station)
    print()

    # TO DO: display most commonly used end station
    popular_end_station =  df['End Station'].value_counts().idxmax()
    n_popular_end_station =  df['End Station'].value_counts().max()
    print('Most Frequent End Station:',popular_end_station)
    print('\tnumber of End Station:',n_popular_end_station)
    print()

    # TO DO: display most frequent combination of start station and end station trip
    popular_comb_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    n_popular_comb_trip = df.groupby(['Start Station', 'End Station']).size().max()
    print()
    print('Most Frequent Combination of Start station and End station:',popular_comb_trip)
    print('\tnumber of Combination:',n_popular_comb_trip)
    print()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = pd.Timedelta(seconds = total_travel_time)
    print('Total Travel Time of Trips:',total_travel_time)
    print()

    # TO DO: display mean travel time
    avr_travel_time = df['Trip Duration'].mean()
    avr_travel_time = pd.Timedelta(seconds = avr_travel_time)
    print('Average Travel Time of Trips:',avr_travel_time)
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count =  df['User Type'].value_counts()
    print('User Type count:')
    print(user_type_count)
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count =  df['Gender'].value_counts()
        print('gender Count:')
        print(gender_count)
        print()
    else:
        print('no gender data')
        print()


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        popular_birth_year = df['Birth Year'].value_counts().idxmax()
        oldest_birth_year = df['Birth Year'].min()
        youngest_birth_year = df['Birth Year'].max()
        print('Most Comman Birth Year:',popular_birth_year)
        print()
        print('Oldest Birth Year:',oldest_birth_year)
        print()
        print('Youngest Birth Year:',youngest_birth_year)
        print()
    else:
        print('no Birth year data')
        print()
     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty == False :
            display_df = input('\nWould you like to display 5 lines of the data? Enter yes or no.\n').lower()
            count = 0
            while display_df == 'yes':
                print(df[count:count+5])
                count += 5
                display_df = input('\nWould you like to display another 5 lines of the data? Enter yes or no.\n').lower()
                     
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
         
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()

