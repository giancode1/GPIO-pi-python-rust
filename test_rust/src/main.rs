use rust_gpiozero::*;
use std::thread::sleep;
use std::time::Duration;

fn main() {
    println!("Hello, world!");

    let led = LED::new(4);  //GPIO4

    loop {
        led.on();
        //delay
        sleep(Duration::from_secs(1));
        led.off();
        //delay
        sleep(Duration::from_secs(1));

    }

}
