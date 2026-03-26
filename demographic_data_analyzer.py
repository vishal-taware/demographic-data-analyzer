import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv('adult.data.csv')

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4 & 5. Advanced education
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # >50K with higher education
    higher_education_rich = round(
        (df[higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # >50K without higher education
    lower_education_rich = round(
        (df[~higher_edu]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. % earning >50K among min workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 8. Country with highest % earning >50K
    country_stats = df.groupby('native-country')['salary'].value_counts(normalize=True)
    rich_country = country_stats[:, '>50K']

    highest_earning_country = rich_country.idxmax()
    highest_earning_country_percentage = round(rich_country.max() * 100, 1)

    # 9. Most popular occupation in India for >50K
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].mode()[0]

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top IN occupation:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
