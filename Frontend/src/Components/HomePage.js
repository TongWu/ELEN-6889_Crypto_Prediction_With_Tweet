import {Button} from 'react-bootstrap';

export const HomePage = () => {

    const clickToBTC = async (e) => {
        e.preventDefault();
        window.location.href="/bitcoin"
    };

    const clickToETH = async (e) => {
        e.preventDefault();
        window.location.href="/ethereum"
    };

    return <>
        <header>
            Welcome
        </header>
        <p></p>

        <div>
            Please choose a cryptocurrency
        </div>
        <p></p>

        <Button onClick={clickToBTC}>BTC</Button>
        <p></p>

        <Button onClick={clickToETH}>ETH</Button>
    </>
}