import Home from './screens/Home';

import {createGlobalStyle} from 'styled-components'

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
  }
`

function App() {
  return (
    <>
      <GlobalStyle/>
      <Home/>
    </>
  );
}

export default App;
