package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	specUrl := "http://200.152.38.155/CNPJ/Empresas0.zip"
	resp, err := http.Get(specUrl)
	if err != nil {
		fmt.Printf("err: %s", err)
	}

	defer resp.Body.Close()
	fmt.Println("status", resp.Status)
	if resp.StatusCode != 200 {
		return
	}

	// Create the file
	out, err := os.Create("test.zip")
	if err != nil {
		fmt.Printf("err: %s", err)
	}
	defer out.Close()

	// Write the body to file
	_, err = io.Copy(out, resp.Body)
	fmt.Printf("err: %s", err)
}
