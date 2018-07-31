import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():
    print_the_header()

    area = input('Please enter an area to check the weather: ')

    html = get_html_from_web(area)

    report = get_weather_from_html(html)

    print('The temp in {} is {}{} and {} '.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))
    # display the forecast


def print_the_header():
    print('-----------------------------')
    print('         WEATHER APP')
    print('-----------------------------')
    print()


def get_html_from_web(area):
    url = 'https://www.wunderground.com/weather/jp/{}'.format(area)
    response = requests.get(url)
    # print(response.status_code)
    #print(response.text)

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-cotent-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(temp, scale, loc, condition)
    #return temp, scale, loc, condition
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()