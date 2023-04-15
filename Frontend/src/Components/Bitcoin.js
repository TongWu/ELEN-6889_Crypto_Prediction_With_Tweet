import {Button, Image} from 'react-bootstrap';
import smile from './smile.png'
import week from './week-image.jpeg';
import month from './month-image.jpeg';
import year from './year-image.jpeg';

export const BitcoinPage = () => {

    const clickToHomePage = async (e) => {
        e.preventDefault();
        window.location.href="/"
    };

    function weekPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = week;
    };

    function monthPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = month;
    };

    function yearPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = year;
    };



    return <>
        <header>
            BTC <Button onClick={clickToHomePage}>Home</Button>
        </header>
        <p></p>

        <div>
            <Image src={smile} id="predictionImage" width="500" height="400"/>
            <p></p>
            <Button onClick={weekPrediction}>Next Week</Button>
            <Button onClick={monthPrediction}>Next Month</Button>
            <Button onClick={yearPrediction}>Next Year</Button>
            <p></p>
        </div>
    </>
}