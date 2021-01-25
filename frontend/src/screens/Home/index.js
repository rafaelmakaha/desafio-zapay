import { FormControlLabel, Checkbox } from '@material-ui/core';
import React, { useEffect, useMemo, useState } from 'react';
import { ConsultaDPVAT, ConsultaIPVA, ConsultaLicenciamento, ConsultaMultas } from '../../services/api';
import { CentralCard, StyledFormGroup, Container, MenuWrapper, ResultsWrapper, Title, TxtField, Text, TxtFieldWrapper} from './style';
import ResultCard from './ResultCard';


const Home = () => {
  const [plate, setPlate] = useState('');
  const [renavam, setRenavam] = useState('');
  const [multas, setMultas] = useState({});
  const [ipva, setIpva] = useState({});
  const [dpvat, setDpvat] = useState({});
  const [licensing, setLicensing] = useState({});
  const [boxes, setBoxes] = useState(['0','1','2','3']);
  const [notFound, setNotFound] = useState(true);

  const labels = useMemo(()=> ['Ticket', 'IPVA', 'DPVAT', 'Licensing'], [])

  const handlePlateChange = (event) => {
    setPlate(event.target.value)
  }

  const handleRenavamChange = (event) => {
    setRenavam(event.target.value)
  }

  const handleBoxChange = (event) => {
    let aux = [...boxes]
    if (event.target.checked){
      aux.push(event.target.name)
    } else {
      aux = aux.filter((name) => name !== event.target.name)
    }
    setBoxes(aux);
  };

  useEffect(() => {
    if (renavam === '11111111111' 
      && (plate.toUpperCase() === 'ABC1234' 
      || plate.toUpperCase() === 'ABC1C34')) {
        setMultas(ConsultaMultas());
        setIpva(ConsultaIPVA());
        setDpvat(ConsultaDPVAT());
        setLicensing(ConsultaLicenciamento());
        setNotFound(false);
    } else {
      setNotFound(true)
    }

  }, [plate, renavam, boxes])

  return (
    <Container>
      <CentralCard>
        <Title>Zapay Challenge</Title>
        <MenuWrapper>
          <TxtFieldWrapper>
            <TxtField label="Placa" onChange={handlePlateChange}/>
            <TxtField label="Renavam" onChange={handleRenavamChange}/>
          </TxtFieldWrapper>
          <StyledFormGroup row>
            {labels.map((label, index) => (
              <FormControlLabel 
              key={index}
              control={
                <Checkbox
                  checked={boxes.includes(String(index))}
                  onChange={handleBoxChange}
                  name={String(index)}
                  color="primary"
                />
              }
              label={label}
            />
            ))}
          </StyledFormGroup>
        </MenuWrapper>
        <ResultsWrapper>
          { notFound 
            ? <Text>Veículo não encontrado</Text> 
            : 
            <> 
              { boxes.includes('0') && 
                <ResultCard title='Multas' texts={multas}/>
              }
              { boxes.includes('1') && 
                <ResultCard title='IPVA' texts={ipva}/>
              }
              { boxes.includes('2') && 
                <ResultCard title='DPVAT' texts={dpvat}/>
              }
              { boxes.includes('3') && 
                <ResultCard title='Licensing' texts={licensing}/>
              }
            </>
          
          }
        </ResultsWrapper>
      </CentralCard>
    </Container>
  )
}

export default Home;