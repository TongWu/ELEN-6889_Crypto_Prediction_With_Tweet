import {Button, Image} from 'react-bootstrap';
import smile from './smile.png'
import day1 from './Prediction_1days.png';
import day3 from './Prediction_3days.png';
import day5 from './Prediction_5days.png';

export const BitcoinPage = () => {

    const clickToHomePage = async (e) => {
        e.preventDefault();
        window.location.href="/"
    };

    function weekPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = day1;
    };
    

    function monthPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = day3;
    };

    function yearPrediction() {
        var image = document.getElementById('predictionImage');
        image.src = day5;
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