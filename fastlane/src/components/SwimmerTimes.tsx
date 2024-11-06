import React, { useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap';

const SwimmerTimes = () => {
  const [times, setTimes] = useState(['', '', '', '']);
  const [showCalculating, setShowCalculating] = useState(false);
  const [fieldsDisabled, setFieldsDisabled] = useState(false);

  const handleTimeChange = (index: number, value: string) => {
    const newTimes = [...times];
    newTimes[index] = value;
    setTimes(newTimes);
  };

  const validateTime = (time: string) => {
    const regex = /^[0-5]?[0-9]:[0-5][0-9]$/; // MM:SS format
    return regex.test(time);
  };

  const handleSubmitTimes = () => {
    for (let time of times) {
      if (!validateTime(time)) {
        alert('Invalid input. Please enter times in MM:SS format.');
        return;
      }
    }
    setShowCalculating(true);
    setFieldsDisabled(true);
  };

  return (
    <>
      <Row>
        {times.map((time, index) => (
          <Col key={index} md={3}>
            <Form.Group controlId={`swimmerTime${index}`}>
              <Form.Label>Swimmer {index + 1} Time</Form.Label>
              <Form.Control
                type="text"
                placeholder="MM:SS"
                value={time}
                onChange={(e) => handleTimeChange(index, e.target.value)}
                disabled={fieldsDisabled}
              />
            </Form.Group>
          </Col>
        ))}
      </Row>
      {!fieldsDisabled && (
        <Button variant="primary" onClick={handleSubmitTimes}>
          Submit Times
        </Button>
      )}
      {showCalculating && (
        <div>
          <p>Calculating ideal swim time...</p>
        </div>
      )}
    </>
  );
};

export default SwimmerTimes;