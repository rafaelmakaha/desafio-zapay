import styled from 'styled-components'
import { FormGroup, TextField } from '@material-ui/core';

export const Container = styled.div`
  background-color: #3242e5;
  display: flex;
  flex-direction: row;
  height: 100%;
  min-height: 100vh;
`
export const CentralCard = styled.div`
  box-shadow: 1.2em;
  background-color: white;
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  padding: 1.2em;
  width: 80%;
`
export const Title = styled.h1`
  text-align: center;
`
export const MenuWrapper = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: 1.2em;
`
export const TxtFieldWrapper = styled.div`
  align-self: center;
  display: flex;
  gap: 1.2em;
`
export const TxtField = styled(TextField)`
  
`
export const StyledFormGroup = styled(FormGroup)`
  justify-content: center;
  
`
export const ResultsWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-content: center;
  margin-top: 1.2em;
  gap: 1.2em;
`
export const Text = styled.p`
  align-self: center;
`