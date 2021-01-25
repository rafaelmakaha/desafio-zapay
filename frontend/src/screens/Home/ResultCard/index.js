import React from 'react'
import { Card, CardContent, Divider } from '@material-ui/core';
import { StyledDivider, Container } from './style'

const ResultCard = ({title, texts=[]}) => {
  return (
    <Container>
      <Card>
        <CardContent>
          <h2>{title}</h2>
          {texts.length ? 
            texts.map((obj, index) => 
            <>
              { 
                Object.entries(obj).map(([key, value], index) => 
                  <p key={index}>{key} : {value}</p>
                )
              }
              {
                texts.length - 1 !== index && 
                <StyledDivider>
                  <Divider />
                </StyledDivider>
              }
            </>
            )
          :
            false
          }
        </CardContent>
      </Card>
    </Container>
  )
};

export default ResultCard;