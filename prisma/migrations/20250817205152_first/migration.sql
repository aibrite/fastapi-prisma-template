-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3),
    "name" VARCHAR(255) NOT NULL,
    "familyName" VARCHAR(255) NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT,
    "roles" TEXT[],
    "provider" TEXT NOT NULL,
    "providerId" TEXT,
    "providerRefreshToken" TEXT,
    "refreshToken" TEXT,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "UserVerifications" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "verification" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3),
    "verifiedAt" TIMESTAMP(3),
    "active" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "UserVerifications_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE INDEX "UserVerifications_userId_verification_idx" ON "UserVerifications"("userId", "verification");

-- AddForeignKey
ALTER TABLE "UserVerifications" ADD CONSTRAINT "UserVerifications_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
