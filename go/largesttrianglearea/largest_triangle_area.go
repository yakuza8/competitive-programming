package largesttrianglearea

import "math"

// You have a list of points in the plane. Return the area of the largest triangle
// that can be formed by any 3 of the points.
//
// Example:
// Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
// Output: 2
// Explanation:
// The five points are show in the figure below. The red triangle is the largest.
func largestTriangleArea(points [][]int) float64 {
	pointCount := len(points)
	maxArea := 0.0
	for i := 2; i < pointCount; i++ {
		for j := 1; j < i; j++ {
			for k := 0; k < j; k++ {
				a := euclideanDistance(points[i], points[j])
				b := euclideanDistance(points[i], points[k])
				c := euclideanDistance(points[j], points[k])
				if isValidTriangle(a, b, c) {
					if area := heronFormula(a, b, c); area > maxArea {
						maxArea = area
					}
				}
			}
		}
	}
	return maxArea
}

func isValidTriangle(a, b, c float64) bool {
	return a+b > c && a+c > b && b+c > a
}

func euclideanDistance(point1, point2 []int) float64 {
	return math.Sqrt(math.Pow(float64(point1[0]-point2[0]), 2) + math.Pow(float64(point1[1]-point2[1]), 2))
}

func heronFormula(a, b, c float64) float64 {
	U := (a + b + c) / 2
	return math.Sqrt(U * (U - a) * (U - b) * (U - c))
}
