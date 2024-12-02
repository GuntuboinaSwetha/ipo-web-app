const data = [
    { label: 'Total IPO', value: 30, color: '#f28c33', radius: 100 },
    { label: 'IPO in Gain', value: 20, color: '#41bfc8', radius: 70 },
    { label: 'IPO in Loss', value: 19, color: '#6a4cbf', radius: 60 }
];

// Select the SVG container for the chart
const svg = d3.select('#ipoChart')
    .attr('width', 400)
    .attr('height', 400);

// Define positions for each circle (avoid overlap)
const positions = [
    { x: 250, y: 170 },  // Total IPO
    { x: 110, y: 260 },  // IPO in Gain
    { x: 110, y: 120 }   // IPO in Loss
];

// Positioning and rendering the circles dynamically
const circles = svg.selectAll('g')
    .data(data)
    .enter()
    .append('g')
    .attr('transform', (d, i) => `translate(${positions[i].x}, ${positions[i].y})`);

// Draw circles
circles.append('circle')
    .attr('r', d => d.radius)
    .style('fill', d => d.color)
    .style('opacity', 0.8);

// Add text to circles
circles.append('text')
    .attr('class', 'circle-text')
    .attr('text-anchor', 'middle')
    .attr('dy', '-0.5em')
    .text(d => d.value)
    .style('fill', '#fff')
    .style('font-size', '1.2em')
    .style('font-weight', 'bold');

// Add labels
circles.append('text')
    .attr('text-anchor', 'middle')
    .attr('dy', '1.5em')
    .text(d => d.label)
    .style('font-size', '0.8em')
    .style('fill', '#fff');
