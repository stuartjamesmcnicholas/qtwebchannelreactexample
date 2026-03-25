import { useEffect, useState } from "react";
import './App.css'
import { QWebChannel } from "qwebchannel";


interface handler {
  id: string;
  "__QObject*__": boolean;
  clicked(name:string): Promise<void>;
}

function App() {

  // @ts-expect-error dummyIgnored is not used
  const dummyClicked = (dummyIgnored:string) => {return new Promise<void>(() =>{})}
  const [bridge,setBridge] = useState<handler>({id:"null","__QObject*__":false, clicked:dummyClicked});

  useEffect(() => {
      // @ts-expect-error window.qt
      new QWebChannel(window.qt.webChannelTransport, function (channel) {
          setBridge(channel.objects.handler)
    });
  }, []);

  const buttonClicked = (name: string) => {
      bridge.clicked(name);
  }

  return (
    <>
    <h2>Hello, world</h2>
       <button title="Show the task menu" id="task_menu" onClick={() => buttonClicked('task_menu')}>Show the task menu</button>
    </>
  )
}

export default App
