import React, { useState } from 'react';
import { Form, Button, Row, Col } from 'react-bootstrap';
import SwimmerTimes from './SwimmerTimes';

const SelectorForm = () => {
  const [showTextBoxes, setShowTextBoxes] = useState(false);
  const [distance, setDistance] = useState('');
  const [stroke, setStroke] = useState('');
  const [ageGroup, setAgeGroup] = useState('');
  const [formDisabled, setFormDisabled] = useState(false);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (distance === '50m' && stroke === 'Freestyle' && ageGroup === '120') {
      setShowTextBoxes(true);
      setFormDisabled(true);
    } else {
      alert('Invalid selection');
      setShowTextBoxes(false);
    }
  };

  return (
    <>
      <Form onSubmit={handleSubmit}>
        <Row>
          <Col md={4}>
            <Form.Select
              aria-label="Select Distance"
              onChange={(e) => setDistance(e.target.value)}
              disabled={formDisabled}
            >
              <option value="">Select Distance</option>
              <option value="50m">50m</option>
              <option value="100m">100m</option>
              {/* Add more options as needed */}
            </Form.Select>
          </Col>
          <Col md={4}>
            <Form.Select
              aria-label="Select Stroke"
              onChange={(e) => setStroke(e.target.value)}
              disabled={formDisabled}
            >
              <option value="">Select Stroke</option>
              <option value="Freestyle">Freestyle</option>
              <option value="Backstroke">Backstroke</option>
              {/* Add more options as needed */}
            </Form.Select>
          </Col>
          <Col md={4}>
            <Form.Select
              aria-label="Select Age Group"
              onChange={(e) => setAgeGroup(e.target.value)}
              disabled={formDisabled}
            >
              <option value="">Select Age Group</option>
              <option value="120">120</option>
              <option value="130">130</option>
              {/* Add more options as needed */}
            </Form.Select>
          </Col>
        </Row>
        {!formDisabled && (
          <Button variant="primary" type="submit">
            Submit
          </Button>
        )}
      </Form>

      {showTextBoxes && <SwimmerTimes />}
    </>
  );
};

export default SelectorForm;