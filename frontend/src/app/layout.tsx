import StoreProvider from "./StoreProvider";
import { Roboto } from "next/font/google";
import type { Metadata } from "next";
import App from "@/components/App";
import "./globals.css";

const roboto = Roboto({
  weight: ["400", "500", "700", "900"],
  subsets: ["latin", "cyrillic"]
});

export const metadata: Metadata = {
  title: "2DuoMinds",
  description: "Generated by create next app",
  manifest: "/manifest.json",
  icons: {
    shortcut: { url: "/favicon.ico", type: "image/x-icon" },
    icon: [
      { url: "/favicon.ico", type: "image/x-icon" },
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon-16x16.png", type: "image/png", sizes: "16x16" },
      { url: "/favicon-32x32.png", type: "image/png", sizes: "32x32" },
      {
        url: "/android-chrome-192x192.png",
        type: "image/png",
        sizes: "192x192",
      },
    ],
    apple: [
      { url: "/apple-touch-icon.png", sizes: "57x57", type: "image/png" },
    ],
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={roboto.className}>
        <StoreProvider>
            <App>
              {children}
            </App>
        </StoreProvider>
      </body>
    </html>
  );
}
